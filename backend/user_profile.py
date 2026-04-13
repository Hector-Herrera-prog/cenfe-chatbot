"""
Sistema de perfilado progresivo del usuario.
Detecta datos clave en cada mensaje y construye el perfil automaticamente.
"""

# Perfiles en memoria por sesion
profiles: dict = {}

def get_profile(session_id: str) -> dict:
    if session_id not in profiles:
        profiles[session_id] = {
            "objetivo": None,          # bajar_peso, ganar_musculo, tonificar, salud, rendimiento
            "experiencia": None,       # principiante, intermedio, avanzado
            "dias_disponibles": None,  # 1-7
            "lesion": None,            # rodilla, espalda, hombro, ninguna
            "condicion_medica": None,  # diabetes, hipertension, ninguna
            "nombre": None,
            "etapa_funnel": "atraccion",  # atraccion, consideracion, perfilado, conversion, fidelizacion, reactivacion
            "es_miembro": False,
            "mensajes_count": 0,
            "intereses": []
        }
    return profiles[session_id]

def update_profile(session_id: str, message: str, intent: str):
    """Detecta datos del usuario en su mensaje y actualiza el perfil"""
    profile = get_profile(session_id)
    msg = message.lower()
    profile["mensajes_count"] += 1

    # Detectar objetivo
    if any(w in msg for w in ["bajar de peso", "perder peso", "adelgazar", "quemar grasa"]):
        profile["objetivo"] = "bajar_peso"
    elif any(w in msg for w in ["ganar musculo", "masa muscular", "volumen", "hipertrofia"]):
        profile["objetivo"] = "ganar_musculo"
    elif any(w in msg for w in ["tonificar", "definir", "marcar"]):
        profile["objetivo"] = "tonificar"
    elif any(w in msg for w in ["salud", "bienestar", "sentirme mejor", "energia"]):
        profile["objetivo"] = "salud"
    elif any(w in msg for w in ["rendimiento", "atletismo", "competencia", "deporte"]):
        profile["objetivo"] = "rendimiento"

    # Detectar experiencia
    if any(w in msg for w in ["principiante", "nunca he ido", "primera vez", "no se nada", "desde cero"]):
        profile["experiencia"] = "principiante"
    elif any(w in msg for w in ["llevo tiempo", "ya entreno", "tengo experiencia", "intermedio"]):
        profile["experiencia"] = "intermedio"
    elif any(w in msg for w in ["avanzado", "llevo anos", "competidor", "atleta"]):
        profile["experiencia"] = "avanzado"

    # Detectar dias disponibles
    for n in ["1", "2", "3", "4", "5", "6", "7"]:
        if f"{n} dia" in msg or f"{n} vez" in msg or f"{n} veces" in msg:
            profile["dias_disponibles"] = int(n)
            break

    # Detectar lesiones
    if any(w in msg for w in ["rodilla", "menisco", "ligamento"]):
        profile["lesion"] = "rodilla"
    elif any(w in msg for w in ["espalda", "lumbar", "columna", "hernia"]):
        profile["lesion"] = "espalda"
    elif any(w in msg for w in ["hombro", "manguito", "rotador"]):
        profile["lesion"] = "hombro"

    # Detectar condicion medica
    if any(w in msg for w in ["diabetes", "diabetico"]):
        profile["condicion_medica"] = "diabetes"
    elif any(w in msg for w in ["presion alta", "hipertension"]):
        profile["condicion_medica"] = "hipertension"

    # Detectar si ya es miembro
    if any(w in msg for w in ["ya soy miembro", "ya estoy inscrito", "ya pago", "mi membresia", "5️⃣"]):
        profile["es_miembro"] = True

    # Actualizar etapa del funnel automaticamente
    profile["etapa_funnel"] = _detectar_etapa(profile, intent)

    return profile

def _detectar_etapa(profile: dict, intent: str) -> str:
    """Determina en que etapa del funnel esta el usuario"""
    count = profile["mensajes_count"]
    es_miembro = profile["es_miembro"]

    if es_miembro:
        return "fidelizacion"

    if intent in ["reactivacion", "desertor_reactivacion"]:
        return "reactivacion"

    if intent in ["inscripcion_nueva", "consulta_precio", "upsell"]:
        return "conversion"

    # Si ya tiene objetivo y experiencia, paso a conversion
    if profile["objetivo"] and profile["experiencia"]:
        return "conversion"

    # Si ya tiene objetivo pero no experiencia, perfilado
    if profile["objetivo"] and count >= 2:
        return "perfilado"

    # Si lleva mas de 1 mensaje, consideracion
    if count >= 2:
        return "consideracion"

    return "atraccion"

def get_profile_context(session_id: str) -> str:
    """Genera el contexto del perfil para el LLM"""
    profile = get_profile(session_id)
    etapa = profile["etapa_funnel"]

    etapas_desc = {
        "atraccion":     "ATRACCION (TOFU) — Usuario nuevo. Conecta emocionalmente, NO vendas directo. Genera confianza y curiosidad.",
        "consideracion": "CONSIDERACION (MOFU) — Usuario interesado. Detecta su problema, pregunta por su objetivo si no lo sabes aun.",
        "perfilado":     "PERFILADO — Personaliza la recomendacion. Pregunta dias disponibles, experiencia o lesiones si faltan datos.",
        "conversion":    "CONVERSION (BOFU) — Listo para cerrar. Invita a clase gratis, presenta el plan ideal, crea urgencia con el bono.",
        "fidelizacion":  "FIDELIZACION — Ya es miembro. Motiva, celebra logros, sugiere retos y mejoras de plan.",
        "reactivacion":  "REACTIVACION — Usuario inactivo. Reconectalo con empatia, ofrece congelar o cambiar plan, no presiones."
    }

    perfil_lines = [f"\n\n=== ETAPA ACTUAL: {etapas_desc[etapa]} ==="]
    perfil_lines.append("PERFIL DEL USUARIO:")

    if profile["objetivo"]:
        perfil_lines.append(f"- Objetivo: {profile['objetivo'].replace('_', ' ')}")
    else:
        perfil_lines.append("- Objetivo: desconocido (pregunta si es relevante)")

    if profile["experiencia"]:
        perfil_lines.append(f"- Experiencia: {profile['experiencia']}")

    if profile["dias_disponibles"]:
        perfil_lines.append(f"- Dias disponibles: {profile['dias_disponibles']} dias/semana")

    if profile["lesion"]:
        perfil_lines.append(f"- Lesion: {profile['lesion']} (adapta ejercicios)")

    if profile["condicion_medica"]:
        perfil_lines.append(f"- Condicion medica: {profile['condicion_medica']} (ten cuidado)")

    perfil_lines.append(f"- Mensajes en conversacion: {profile['mensajes_count']}")

    perfil_lines.append("\nINSTRUCCION: Adapta tu respuesta a la etapa y perfil. Sigue el flujo natural del funnel.")

    return "\n".join(perfil_lines)

def reset_profile(session_id: str):
    if session_id in profiles:
        del profiles[session_id]
