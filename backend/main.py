from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
import json
import os
from dotenv import load_dotenv

load_dotenv()

from vectordb.vector_store import find_best_intent, seed_knowledge_base
from llm_handler import get_ai_response, stream_ai_response, get_quick_replies, extract_quick_replies_from_stream
from knowledge.responses import RESPONSES
from user_profile import get_profile_context, update_profile, reset_profile

app = FastAPI(title="CENFE FitBot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

conversations: dict = {}

class Message(BaseModel):
    session_id: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    session_id: str
    response: str
    quick_replies: List[str]
    intent: str
    confidence: float

@app.on_event("startup")
async def startup_event():
    print("Iniciando CENFE FitBot...")
    try:
        seed_knowledge_base()
        print("Base de conocimiento lista!")
    except Exception as e:
        print(f"Error al inicializar vector DB: {e}")

@app.post("/chat", response_model=ChatResponse)
async def chat(msg: Message):
    session_id = msg.session_id or str(uuid.uuid4())
    if session_id not in conversations:
        conversations[session_id] = []
    history = conversations[session_id]

    intent_result = find_best_intent(msg.message)
    response_key = intent_result.get("response_key", None)
    intent = intent_result.get("intent", "general")

    profile_context = get_profile_context(session_id)
    update_profile(session_id, msg.message, intent)

    ai_response, quick_replies = get_ai_response(
        user_message=msg.message,
        conversation_history=history,
        response_key=response_key,
        profile_context=profile_context
    )

    history.append({"role": "user", "content": msg.message})
    history.append({"role": "assistant", "content": ai_response})
    if len(history) > 20:
        conversations[session_id] = history[-20:]

    return ChatResponse(
        session_id=session_id,
        response=ai_response,
        quick_replies=quick_replies,
        intent=intent,
        confidence=intent_result.get("confidence", 0)
    )

@app.post("/chat/stream")
async def chat_stream(msg: Message):
    session_id = msg.session_id or str(uuid.uuid4())
    if session_id not in conversations:
        conversations[session_id] = []

    history = conversations[session_id]
    intent_result = find_best_intent(msg.message)
    response_key = intent_result.get("response_key", None)
    intent = intent_result.get("intent", "general")

    profile_context = get_profile_context(session_id)
    update_profile(session_id, msg.message, intent)

    full_response = []

    def event_stream():
        meta = {
            "type": "meta",
            "session_id": session_id,
            "intent": intent,
            "quick_replies": []
        }
        yield f"data: {json.dumps(meta, ensure_ascii=False)}\n\n"

        for token in stream_ai_response(msg.message, history, response_key, profile_context):
            full_response.append(token)
            if "OPCIONES:" not in token:
                payload = {"type": "token", "value": token}
                yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"

        complete_text = "".join(full_response)
        clean_text, quick_replies = extract_quick_replies_from_stream(complete_text, response_key)

        history.append({"role": "user", "content": msg.message})
        history.append({"role": "assistant", "content": clean_text})
        if len(history) > 20:
            conversations[session_id] = history[-20:]

        yield f"data: {json.dumps({'type': 'done', 'quick_replies': quick_replies})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.post("/reset/{session_id}")
async def reset_conversation(session_id: str):
    if session_id in conversations:
        del conversations[session_id]
    reset_profile(session_id)
    return {"status": "ok", "message": "Conversacion reiniciada"}

@app.get("/health")
async def health():
    return {"status": "ok", "service": "CENFE FitBot"}

@app.get("/intents")
async def list_intents():
    from knowledge.cenfe_knowledge import USE_CASES
    return {"total": len(USE_CASES), "intents": list(USE_CASES.keys())}
