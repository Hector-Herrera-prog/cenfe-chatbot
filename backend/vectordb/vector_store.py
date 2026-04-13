import chromadb
from chromadb.utils import embedding_functions
import os
from pathlib import Path

CHROMA_PATH = os.getenv("CHROMA_DB_PATH", "./vectordb/chroma_data")

# Usar embeddings ONNX de ChromaDB — no necesita PyTorch, mucho mas ligero
embedding_fn = embedding_functions.ONNXMiniLM_L6_V2()

_client = None
_collection = None

def get_collection():
    global _client, _collection
    if _collection is None:
        Path(CHROMA_PATH).mkdir(parents=True, exist_ok=True)
        _client = chromadb.PersistentClient(path=CHROMA_PATH)
        _collection = _client.get_or_create_collection(
            name="cenfe_knowledge",
            embedding_function=embedding_fn,
            metadata={"hnsw:space": "cosine"}
        )
    return _collection

def seed_knowledge_base():
    """Poblar la base vectorial con el conocimiento de CENFE"""
    from knowledge.cenfe_knowledge import USE_CASES, CENFE_INFO
    
    collection = get_collection()
    
    # Verificar si ya tiene datos
    if collection.count() > 0:
        print(f"Vector DB ya tiene {collection.count()} documentos")
        return
    
    documents = []
    metadatas = []
    ids = []
    
    for case_id, case_data in USE_CASES.items():
        for i, trigger in enumerate(case_data["triggers"]):
            doc_id = f"{case_id}_{i}"
            documents.append(trigger)
            metadatas.append({
                "case_id": case_id,
                "intent": case_data["intent"],
                "response_key": case_data["response_key"]
            })
            ids.append(doc_id)
    
    # Agregar info general del gym
    gym_docs = [
        "cuanto cuesta la membresia precio planes",
        "horarios del gym cuando abren cierran",
        "donde estan ubicados sucursales direccion",
        "como me inscribo registro membresia",
        "que incluye la membresia beneficios",
        "clases grupales spinning zumba yoga pilates",
        "entrenador personal coach",
        "nutricion dieta alimentacion",
        "congelar pausar membresia",
        "cancelar membresia baja"
    ]
    
    for i, doc in enumerate(gym_docs):
        documents.append(doc)
        metadatas.append({
            "case_id": "general_info",
            "intent": "info_general",
            "response_key": "default"
        })
        ids.append(f"general_{i}")
    
    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"Vector DB poblada con {len(documents)} documentos")

def find_best_intent(user_message: str, n_results: int = 3) -> dict:
    """Buscar el intent mas relevante para el mensaje del usuario"""
    collection = get_collection()
    
    results = collection.query(
        query_texts=[user_message],
        n_results=min(n_results, collection.count())
    )
    
    if not results["metadatas"] or not results["metadatas"][0]:
        return {"intent": "general", "response_key": None, "confidence": 0}
    
    best_match = results["metadatas"][0][0]
    distance = results["distances"][0][0] if results["distances"] else 1.0
    confidence = 1 - distance

    # Si la confianza es muy baja, devolver None como response_key
    # para que el LLM responda libremente sin respuesta predefinida
    if confidence < 0.3:
        return {"intent": "general", "response_key": None, "confidence": round(confidence, 3)}
    
    return {
        "intent": best_match.get("intent", "general"),
        "response_key": best_match.get("response_key", None),
        "case_id": best_match.get("case_id", "general"),
        "confidence": round(confidence, 3)
    }
