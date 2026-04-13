# CENFE FitBot

Chat inteligente con 50 casos de uso, ChromaDB vectorial y MCP para diagramas. Todo 100% gratuito.

## Stack

| Componente | Tecnologia | Costo |
|---|---|---|
| Frontend | HTML/CSS/JS | Gratis |
| Backend | Python + FastAPI | Gratis |
| LLM | Groq API llama3-70b | Gratis |
| Vector DB | ChromaDB local | Gratis |
| Embeddings | sentence-transformers | Gratis |
| Diagramas | PlantUML via MCP | Gratis |

## Instalacion (Windows)

**1. Obtener API Key de Groq (GRATIS)**
- Ve a https://console.groq.com → crea cuenta → genera API Key

**2. Instalar**
```bash
cd cenfe-chatbot
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt
```

**3. Configurar**
```bash
copy .env.example .env
# Edita .env y pon tu GROQ_API_KEY
```

**4. Iniciar backend**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**5. Abrir chat**
Abre `frontend/index.html` en el navegador.

## MCP en Kiro

Agrega en `~/.kiro/settings/mcp.json`:
```json
{
  "mcpServers": {
    "cenfe-diagrams": {
      "command": "python",
      "args": ["C:/ruta/cenfe-chatbot/backend/mcp/diagrams_server.py"],
      "disabled": false,
      "autoApprove": ["generate_use_case_diagram", "list_use_cases"]
    }
  }
}
```

Luego en Kiro puedes pedir: "Genera el diagrama del bloque de adquisicion"

## 50 Casos de Uso

A-Adquisicion (9) | B-Servicio (3) | C-Retencion (4) | D-Psicologia (5)
E-Onboarding (3) | F-Entrenamiento (3) | G-Nutricion (3) | H-Salud (3)
I-Engagement (4) | J-Personalizacion (2) | K-Admin (3) | L-Social (2)
M-Ventas Avanzadas (3) | N-IA Avanzada (3)

## API

- `POST /chat` - Enviar mensaje
- `POST /reset/{session_id}` - Reiniciar sesion
- `GET /health` - Estado
- `GET /intents` - Listar intents
