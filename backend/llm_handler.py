import os
import json
from typing import Generator
from groq import Groq
from knowledge.responses import RESPONSES
from knowledge.cenfe_knowledge import CENFE_INFO

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

SYSTEM_PROMPT = """Eres FitBot, el asistente virtual del Gym CENFE.
Tu personalidad es: MUY motivador, energico, entusiasta, cercano y apasionado por el fitness.
Hablas como un coach que genuinamente quiere que la gente logre sus metas.
Siempre respondes en espanol.
Tu objetivo es ayudar, motivar e inspirar a los usuarios, y convertir consultas en inscripciones.

Informacion del gym:
- Nombre: Gym CENFE
- Slogan: "Tu mejor version empieza aqui"
- Planes: Basico ($299/mes), Welcome ($399/mes), Premium ($599/mes), Elite ($899/mes)
- Horarios: Lun-Vie 5am-11pm | Sab 6am-9pm | Dom 7am-6pm
- Sucursales: Norte, Sur, Centro
- Clase de prueba: GRATIS para nuevos miembros
- Congelacion: hasta 3 meses sin costo
- Referidos: 1 mes gratis por cada amigo inscrito
- Bono actual: inscripcion gratis + plan nutricional basico si se inscriben hoy

Reglas IMPORTANTES:
1. USA emojis en cada mensaje para darle energia y vida (3-5 emojis por respuesta)
2. Usa MAYUSCULAS ocasionalmente para enfatizar palabras clave
3. LEE con cuidado lo que el usuario escribio, aunque tenga errores de ortografia o typos
4. Responde SIEMPRE en relacion directa a lo que el usuario pregunto o dijo
5. Usa el historial de conversacion para entender el contexto y continuar el hilo
6. Si preguntan por inscripcion o membresia, explica los planes con entusiasmo
7. Si preguntan precio, primero presenta el valor increible y luego el precio
8. Si preguntan horarios, da los horarios exactos
9. Si el mensaje tiene errores tipograficos, interpreta la intencion correcta
10. Tono: como un amigo apasionado por el fitness que quiere verte triunfar
11. Siempre termina con una pregunta o call to action que genere accion inmediata
12. Maximo 130 palabras por respuesta
13. Usa **negritas** para destacar informacion importante
14. NUNCA respondas con el saludo inicial si ya hay una conversacion en curso
15. Si el usuario escribe un numero (1-5), interpreta la opcion del menu de bienvenida"""

QUICK_REPLIES_PROMPT = """

Ademas de tu respuesta, genera exactamente 3 opciones de respuesta rapida COHERENTES con lo que acabas de decir.
Formato OBLIGATORIO en la ultima linea:
OPCIONES: opcion1 | opcion2 | opcion3"""

def _build_messages(user_message, conversation_history, response_key, profile_context=""):
    intent_hint = ""
    if response_key and response_key in RESPONSES:
        predefined = RESPONSES[response_key]["message"]
        intent_hint = f"\n\nTema detectado: {response_key}. Referencia util: {predefined[:200]}"

    messages = [{"role": "system", "content": SYSTEM_PROMPT + profile_context + intent_hint + QUICK_REPLIES_PROMPT}]
    for msg in conversation_history[-8:]:
        messages.append(msg)
    messages.append({"role": "user", "content": user_message})
    return messages

def get_ai_response(user_message: str, conversation_history: list, response_key: str = None, profile_context: str = "") -> tuple:
    messages = _build_messages(user_message, conversation_history, response_key, profile_context)
    try:
        response = client.chat.completions.create(
            model=MODEL, messages=messages, max_tokens=400, temperature=0.7
        )
        return _parse_response(response.choices[0].message.content, response_key)
    except Exception as e:
        print(f"Error Groq: {e}")
        fallback = RESPONSES.get(response_key, RESPONSES["default"])["message"] if response_key else "Hola! En que te puedo ayudar? 💪"
        return fallback, RESPONSES.get(response_key, RESPONSES["default"]).get("quick_replies", [])

def stream_ai_response(user_message: str, conversation_history: list, response_key: str = None, profile_context: str = ""):
    messages = _build_messages(user_message, conversation_history, response_key, profile_context)
    try:
        stream = client.chat.completions.create(
            model=MODEL, messages=messages, max_tokens=400, temperature=0.7, stream=True
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
    except Exception as e:
        print(f"Error Groq stream: {e}")
        yield "Lo siento, hubo un problema. Por favor intenta de nuevo. 💪"

def _parse_response(full_text: str, response_key: str = None) -> tuple:
    """Separa el texto de la respuesta de la linea OPCIONES"""
    lines = full_text.strip().split("\n")
    quick_replies = []
    clean_lines = []

    for line in lines:
        if line.strip().startswith("OPCIONES:"):
            raw = line.replace("OPCIONES:", "").strip()
            quick_replies = [q.strip() for q in raw.split("|") if q.strip()][:3]
        else:
            clean_lines.append(line)

    # Si el LLM no genero opciones, usar las predefinidas
    if not quick_replies and response_key and response_key in RESPONSES:
        quick_replies = RESPONSES[response_key].get("quick_replies", [])

    return "\n".join(clean_lines).strip(), quick_replies

def extract_quick_replies_from_stream(full_text: str, response_key: str = None) -> tuple:
    """Extrae quick replies del texto completo generado por stream"""
    return _parse_response(full_text, response_key)

def get_quick_replies(response_key: str) -> list:
    if response_key in RESPONSES:
        return RESPONSES[response_key].get("quick_replies", [])
    return RESPONSES["default"].get("quick_replies", [])
