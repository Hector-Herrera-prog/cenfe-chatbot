# REPORTE COMPLETO — CENFE FitBot
**Proyecto:** Chatbot de ventas y servicio para Gym CENFE  
**Fecha:** Abril 2026  
**Desarrollado con:** Kiro AI + Python + FastAPI + ChromaDB + Groq + AWS S3 + Railway

---

## 1. DESCRIPCION GENERAL

Se construyo desde cero un chatbot inteligente para el Gym CENFE llamado **FitBot**. El bot es capaz de atender a clientes potenciales y miembros actuales del gym, guiarlos a traves de un funnel de ventas completo, responder preguntas, motivarlos y convertir consultas en inscripciones. Todo el stack tecnologico utilizado es **100% gratuito**.

---

## 2. STACK TECNOLOGICO

| Componente | Tecnologia | Funcion | Costo |
|---|---|---|---|
| Frontend | HTML + CSS + JavaScript puro | Interfaz del chat | Gratis |
| Backend | Python 3.11 + FastAPI | Servidor de la API | Gratis |
| LLM | Groq API (llama-3.3-70b-versatile) | Generacion de respuestas IA | Gratis |
| Vector DB | ChromaDB local | Busqueda semantica de intents | Gratis |
| Embeddings | ONNX MiniLM L6 V2 | Conversion de texto a vectores | Gratis |
| Hosting Backend | Railway | Servidor 24/7 en la nube | Gratis |
| Hosting Frontend | AWS S3 | Sitio web estatico publico | Gratis |
| Diagramas | PlantUML via MCP | Generacion de diagramas UML | Gratis |
| Control de versiones | Git + GitHub | Repositorio del codigo | Gratis |

---

## 3. ARQUITECTURA DEL SISTEMA

```
Usuario (celular o PC)
        |
        v
AWS S3 — Frontend (index.html)
http://cenfe-fitbot-chat.s3-website.us-east-2.amazonaws.com
        |
        v (HTTPS)
Railway — Backend FastAPI
https://cenfe-chatbot-production.up.railway.app
        |
        +---> ChromaDB (busqueda vectorial de intents)
        |
        +---> Groq API (generacion de respuesta con LLM)
        |
        +---> user_profile.py (sistema de perfilado)
        |
        v
Respuesta en streaming al usuario
```

---

## 4. ESTRUCTURA DE ARCHIVOS

```
cenfe-chatbot/
├── frontend/
│   └── index.html              # Chat UI completo
├── backend/
│   ├── main.py                 # FastAPI — endpoints /chat/stream, /reset, /health
│   ├── llm_handler.py          # Integracion con Groq LLM + streaming
│   ├── user_profile.py         # Sistema de perfilado y funnel
│   ├── requirements.txt        # Dependencias Python
│   ├── knowledge/
│   │   ├── cenfe_knowledge.py  # 50 casos de uso con triggers
│   │   └── responses.py        # Respuestas predefinidas de referencia
│   ├── vectordb/
│   │   └── vector_store.py     # ChromaDB — seed y busqueda semantica
│   └── mcp/
│       └── diagrams_server.py  # Servidor MCP para diagramas PlantUML
├── .env                        # Variables de entorno (API keys)
├── .env.example                # Plantilla de variables
├── .gitignore                  # Archivos excluidos de Git
├── Procfile                    # Comando de inicio para Railway
├── nixpacks.toml               # Configuracion de build para Railway
├── requirements.txt            # Copia en raiz para Railway
├── runtime.txt                 # Version de Python para Railway
├── iniciar_bot.bat             # Script de inicio local con doble clic
└── README.md                   # Documentacion del proyecto
```

---

## 5. CASOS DE USO IMPLEMENTADOS (50 TOTAL)

### BLOQUE A — Adquisicion (9 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC01 | Inscripcion Nueva | Usuario quiere inscribirse al gym |
| UC02 | Principiante Nuevo | Usuario sin experiencia previa |
| UC03 | Atleta Estancado | Usuario que no ve progreso |
| UC04 | Reactivacion Desertor | Usuario que dejo de ir y quiere volver |
| UC05 | Consulta de Precio | Usuario pregunta por costos |
| UC06 | Miedo a las Pesas | Usuario teme ponerse muy musculoso |
| UC07 | Horarios y Sucursales | Usuario pregunta logistica |
| UC08 | Clases con Cupo | Usuario quiere reservar clase grupal |
| UC09 | Venta en Pareja/Grupo | Usuario quiere inscribir a varios |

### BLOQUE B — Servicio (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC10 | Congelacion de Membresia | Usuario necesita pausar |
| UC11 | Cross-sell Nutricion | Ofrecer plan nutricional a miembro |
| UC12 | Gestion de Quejas | Atender problemas del usuario |

### BLOQUE C — Retencion (4 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC13 | Felicitacion por Logro | Gamificacion y celebracion |
| UC14 | Encuesta de Calidad | Recopilar feedback |
| UC15 | Programa de Referidos | Traer amigos al gym |
| UC16 | Reporte de Progreso | Evaluacion fisica del miembro |

### BLOQUE D — Psicologia (5 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC17 | Sin Tiempo | Usuario muy ocupado |
| UC18 | Pena/Inseguridad | Usuario con miedo al juicio social |
| UC19 | Abandono Recurrente | Usuario que siempre deja el gym |
| UC20 | Sin Resultados | Usuario frustrado |
| UC21 | Baja Motivacion | Usuario con flojera |

### BLOQUE E — Onboarding (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC22 | Primer Dia en Gym | Guia para el primer dia |
| UC23 | Tour Virtual | Descripcion de instalaciones |
| UC24 | Explicacion de Maquinas | Educacion sobre equipos |

### BLOQUE F — Entrenamiento (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC25 | Rutina Personalizada | Generacion de plan de ejercicios |
| UC26 | Ajuste de Rutina | Progresion del entrenamiento |
| UC27 | Rutina en Casa | Alternativa sin equipo |

### BLOQUE G — Nutricion Avanzada (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC28 | Plan Semanal | Menu nutricional completo |
| UC29 | Sustituciones | Alternativas alimenticias |
| UC30 | Control de Calorias | Calculo de TDEE y macros |

### BLOQUE H — Salud (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC31 | Lesiones Especificas | Protocolo para lesiones |
| UC32 | Enfermedades | Adaptacion para condiciones medicas |
| UC33 | Rehabilitacion | Programa post-cirugia |

### BLOQUE I — Engagement (4 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC34 | Recordatorios Inteligentes | Notificaciones de entrenamiento |
| UC35 | Rachas (Streaks) | Dias consecutivos de entrenamiento |
| UC36 | Retos Mensuales | Competencias internas |
| UC37 | Ranking de Usuarios | Tabla de posiciones |

### BLOQUE J — Personalizacion (2 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC38 | Recomendacion de Plan | Quiz para elegir membresia |
| UC39 | Adaptacion de Tono | Motivador vs tecnico |

### BLOQUE K — Admin (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC40 | Acceso QR | Codigo de entrada al gym |
| UC41 | Historial de Asistencia | Registro de visitas |
| UC42 | Pagos Automaticos | Configuracion de cobro |

### BLOQUE L — Social (2 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC43 | Buscar Companero | Workout buddy |
| UC44 | Eventos Especiales | Clases tematicas y competencias |

### BLOQUE M — Ventas Avanzadas (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC45 | Upsell Automatico | Cambio a plan superior |
| UC46 | Ofertas Personalizadas | Descuentos segun perfil |
| UC47 | Urgencia Dinamica | Ultimos lugares disponibles |

### BLOQUE N — IA Avanzada (3 casos)
| ID | Caso de Uso | Descripcion |
|---|---|---|
| UC48 | Prediccion de Abandono | Detecta riesgo de cancelacion |
| UC49 | Coaching IA | Sesion personalizada continua |
| UC50 | Ajuste de Objetivos | Evolucion de metas del usuario |

---

## 6. BASE DE DATOS VECTORIAL (ChromaDB)

### Que es y como funciona
ChromaDB es una base de datos vectorial que almacena los 50 casos de uso como vectores numericos. Cuando el usuario escribe un mensaje, el sistema:

1. Convierte el mensaje del usuario en un vector numerico usando ONNX MiniLM
2. Busca en ChromaDB los vectores mas similares (busqueda por similitud coseno)
3. Devuelve el intent con mayor similitud
4. Pasa ese intent al LLM como contexto

### Datos almacenados
- **476 documentos** en total (triggers de los 50 casos de uso)
- Cada caso de uso tiene entre 8 y 15 triggers diferentes
- Los triggers cubren variaciones de escritura, sinonimos y errores tipograficos
- Umbral de confianza: si la similitud es menor a 0.3, el LLM responde libremente

### Ubicacion
```
backend/vectordb/chroma_data/chroma.sqlite3
```

### Modelo de embeddings
- **Local:** ONNX MiniLM L6 V2 (incluido en ChromaDB)
- No requiere PyTorch ni conexion a internet
- Tamano: ~50MB vs 2GB de sentence-transformers

---

## 7. SISTEMA DE PERFILADO Y FUNNEL DE VENTAS

### Las 7 etapas implementadas

| Etapa | Nombre | Objetivo del Bot |
|---|---|---|
| 1 | ATRACCION (TOFU) | Conectar emocionalmente, NO vender directo |
| 2 | CONSIDERACION (MOFU) | Detectar problema y objetivo del usuario |
| 3 | PERFILADO | Recopilar datos: objetivo, experiencia, dias, lesiones |
| 4 | CONVERSION (BOFU) | Cerrar venta, invitar a clase gratis |
| 5 | SEGUIMIENTO | Mantener contacto post-inscripcion |
| 6 | FIDELIZACION | Motivar, celebrar logros, retener miembro |
| 7 | REACTIVACION | Recuperar usuarios inactivos |

### Datos que el bot detecta automaticamente
- **Objetivo:** bajar peso, ganar musculo, tonificar, salud, rendimiento
- **Experiencia:** principiante, intermedio, avanzado
- **Dias disponibles:** 1 a 7 dias por semana
- **Lesiones:** rodilla, espalda, hombro
- **Condicion medica:** diabetes, hipertension
- **Si ya es miembro:** detectado por palabras clave

### Como avanza el funnel
El sistema detecta automaticamente en que etapa esta el usuario basandose en:
- Numero de mensajes en la conversacion
- Datos del perfil ya recopilados
- Intent detectado por ChromaDB

---

## 8. SISTEMA DE STREAMING

### Problema que resuelve
Sin streaming, el usuario esperaba 3-5 segundos sin ver nada hasta que Groq terminaba de generar la respuesta completa.

### Solucion implementada
Se implemento **Server-Sent Events (SSE)** — el backend envia cada token (palabra) al frontend en tiempo real conforme Groq los genera.

### Flujo tecnico
```
Usuario envia mensaje
        |
        v
Backend detecta intent en ChromaDB (~50ms)
        |
        v
Backend inicia stream con Groq
        |
        v (token por token)
Frontend recibe y muestra cada palabra al instante
        |
        v
Al terminar, extrae quick replies de la respuesta
```

### Resultado
La respuesta aparece palabra por palabra igual que ChatGPT, dando sensacion de respuesta instantanea.

---

## 9. QUICK REPLIES DINAMICOS

### Problema original
Los botones de respuesta rapida eran estaticos y no tenian relacion con lo que el bot acababa de responder.

### Solucion implementada
El LLM genera sus propios quick replies al final de cada respuesta usando el formato:
```
OPCIONES: opcion1 | opcion2 | opcion3
```

El backend extrae esta linea, la elimina del texto visible y la envia como quick replies al frontend. Resultado: los botones siempre son coherentes con el contexto de la conversacion.

---

## 10. PLANES DEL GYM CENFE

| Plan | Precio | Incluye |
|---|---|---|
| Basico | $299/mes | Acceso a maquinas, vestidores, casillero |
| Welcome | $399/mes | Todo Basico + induccion con entrenador, tour, app con videos, grupo principiantes |
| Premium | $599/mes | Todo Welcome + clases grupales ilimitadas, evaluacion fisica mensual, nutricion basica |
| Elite | $899/mes | Todo Premium + entrenador personal 2x semana, plan nutricional personalizado, acceso multiclub |

**Bono actual:** Inscripcion gratis + plan nutricional basico si se inscriben en 24 horas.

---

## 11. ENDPOINTS DE LA API

| Metodo | Endpoint | Descripcion |
|---|---|---|
| POST | /chat/stream | Enviar mensaje (streaming SSE) |
| POST | /chat | Enviar mensaje (respuesta completa) |
| POST | /reset/{session_id} | Reiniciar conversacion y perfil |
| GET | /health | Estado del servicio |
| GET | /intents | Listar todos los intents |

---

## 12. MCP PARA DIAGRAMAS

Se implemento un servidor MCP (Model Context Protocol) que permite generar diagramas de casos de uso directamente desde el chat de Kiro.

### Herramientas disponibles
- `generate_use_case_diagram` — genera diagrama PlantUML de cualquier bloque
- `list_use_cases` — lista los 50 casos de uso organizados por bloque

### Bloques disponibles para diagramar
all, adquisicion, servicio, retencion, psicologia, entrenamiento, nutricion, salud, engagement, ventas_avanzadas

### Configuracion
```json
{
  "mcpServers": {
    "cenfe-diagrams": {
      "command": "C:/Users/hecto/Documents/Kiro/cenfe-chatbot/venv/Scripts/python.exe",
      "args": ["C:/Users/hecto/Documents/Kiro/cenfe-chatbot/backend/mcp/diagrams_server.py"],
      "disabled": false,
      "autoApprove": ["generate_use_case_diagram", "list_use_cases"]
    }
  }
}
```

---

## 13. DESPLIEGUE EN PRODUCCION

### Backend — Railway
- **URL:** https://cenfe-chatbot-production.up.railway.app
- **Plataforma:** Railway (gratis, 500 horas/mes)
- **Runtime:** Python 3.11
- **Variables de entorno configuradas:** GROQ_API_KEY, GROQ_MODEL, CHROMA_DB_PATH
- **Auto-deploy:** cada push a GitHub actualiza el servidor automaticamente

### Frontend — AWS S3
- **URL:** http://cenfe-fitbot-chat.s3-website.us-east-2.amazonaws.com
- **Plataforma:** AWS S3 Static Website Hosting (gratis, 5GB free tier)
- **Region:** us-east-2 (Ohio)
- **Acceso:** publico, cualquier persona con el link puede usarlo

### Repositorio GitHub
- **Usuario:** Hector-Herrera-prog
- **Repo:** cenfe-chatbot
- **URL:** https://github.com/Hector-Herrera-prog/cenfe-chatbot

---

## 14. USO LOCAL (sin internet)

Para usar el bot localmente sin depender de Railway:

1. Doble clic en `iniciar_bot.bat`
2. Esperar que aparezca "Application startup complete"
3. El chat se abre automaticamente en el navegador

El archivo `.bat` hace automaticamente:
- Activa el entorno virtual Python
- Inicia uvicorn en puerto 8000
- Abre frontend/index.html en el navegador

---

## 15. PROBLEMAS RESUELTOS DURANTE EL DESARROLLO

| Problema | Causa | Solucion |
|---|---|---|
| Conflicto de dependencias pydantic | mcp==1.0.0 requeria pydantic>=2.8.0 | Cambiar a pydantic>=2.8.0 |
| numpy incompatible con chromadb | numpy 2.x elimino np.float_ | Bajar a numpy<2.0 |
| Modelo LLM deprecado | llama3-70b-8192 fue retirado por Groq | Cambiar a llama-3.3-70b-versatile |
| Rate limit de Groq | 100,000 tokens/dia en plan gratuito | Crear nueva API key |
| Build fallido en Railway (Railpack) | requirements.txt no estaba en raiz | Copiar requirements.txt a raiz |
| Build fallido en Railway (5.7GB) | torch/sentence-transformers muy pesados | Cambiar a ONNX embeddings de ChromaDB |
| Bot no cargaba en celular | index.html desactualizado en S3 | Volver a subir index.html a S3 |
| MCP no conectaba en Kiro | Usaba Python del sistema sin librerias | Apuntar al Python del venv |

---

## 16. MEJORAS FUTURAS SUGERIDAS

| Mejora | Descripcion | Dificultad |
|---|---|---|
| Dominio personalizado | fitbot.cenfe.com en lugar de URL de S3 | Baja |
| WhatsApp Business | Conectar bot a WhatsApp via Twilio | Media |
| Panel de administracion | Ver conversaciones y estadisticas en tiempo real | Alta |
| Base de datos de usuarios | Guardar perfiles entre sesiones (PostgreSQL) | Media |
| Notificaciones proactivas | Bot que manda mensajes sin que el usuario escriba | Alta |
| Integracion de pagos | Cobrar membresia directamente desde el chat | Alta |
| Multiidioma | Soporte para ingles | Baja |

---

## 18. PLATAFORMAS Y SERVICIOS UTILIZADOS

### 1. Groq — https://console.groq.com
**Funcion:** Es el "cerebro" del bot. Groq es un servicio de IA que da acceso al modelo de lenguaje LLaMA 3 de Meta de forma gratuita.
- Genera todas las respuestas del bot de forma natural e inteligente
- Usa hardware especializado llamado LPU (Language Processing Unit) que lo hace el LLM mas rapido disponible gratuitamente
- Genera aproximadamente 800 palabras por segundo
- **Plan gratuito:** 100,000 tokens por dia, sin tarjeta de credito
- **Modelo usado:** llama-3.3-70b-versatile
- **Como se usa:** Se obtiene una API Key desde el panel y se configura en el archivo .env

---

### 2. Railway — https://railway.app
**Funcion:** Hospeda el backend (servidor Python) en la nube 24/7.
- Sin Railway, el bot solo funcionaba cuando la laptop estaba encendida
- Railway descarga el codigo desde GitHub y lo ejecuta en sus servidores automaticamente
- Cada vez que se hace un `git push`, Railway actualiza el servidor solo
- **Plan gratuito:** 500 horas al mes + $5 USD de credito inicial
- **Como se usa:** Se conecta con GitHub, se configuran las variables de entorno (API keys) y se hace deploy con un clic

---

### 3. AWS S3 — https://aws.amazon.com/s3
**Funcion:** Hospeda el frontend (index.html) publicamente en internet.
- Permite que cualquier persona abra el chat desde su celular o PC con un link
- S3 es un servicio de almacenamiento de archivos de Amazon que puede servir paginas web estaticas
- **URL generada:** http://cenfe-fitbot-chat.s3-website.us-east-2.amazonaws.com
- **Plan gratuito:** 5 GB de almacenamiento, 20,000 solicitudes de lectura al mes (primer año)
- **Como se usa:** Se crea un bucket, se habilita el hosting estatico, se desactiva el bloqueo publico, se agrega una politica de acceso y se sube el index.html

---

### 4. GitHub — https://github.com
**Funcion:** Repositorio del codigo en la nube.
- Guarda todo el codigo del proyecto de forma segura
- Permite que Railway descargue el codigo automaticamente
- Cada cambio queda registrado con historial completo
- **Plan gratuito:** repositorios publicos y privados ilimitados
- **Repositorio:** https://github.com/Hector-Herrera-prog/cenfe-chatbot
- **Como se usa:** Se inicializa Git en la carpeta del proyecto, se conecta al repositorio remoto y se sube con `git push`

---

### 5. PlantUML — https://www.plantuml.com
**Funcion:** Genera diagramas de casos de uso en formato de imagen.
- Convierte codigo de texto en diagramas UML visuales
- Se usa a traves del servidor MCP desde Kiro
- No requiere instalacion, usa el servidor publico gratuito de PlantUML
- **Plan gratuito:** uso ilimitado del servidor publico
- **Como se usa:** El servidor MCP genera el codigo PlantUML, lo codifica en Base64 y construye una URL que devuelve la imagen del diagrama

---

### 6. Kiro — IDE de desarrollo
**Funcion:** Entorno de desarrollo donde se construyo todo el proyecto.
- Se uso para escribir y editar todo el codigo
- Se configuro el servidor MCP de diagramas directamente en Kiro
- Permite pedir diagramas de casos de uso desde el chat con lenguaje natural
- **Como se usa:** Workspace local con acceso a todas las herramientas de desarrollo

---

### 7. ChromaDB — https://www.trychroma.com
**Funcion:** Base de datos vectorial local para busqueda semantica.
- Almacena los 476 triggers de los 50 casos de uso como vectores numericos
- Cuando el usuario escribe, busca el trigger mas similar semanticamente
- Corre completamente en la maquina local / servidor de Railway, sin costo externo
- **Plan gratuito:** completamente open source y gratuito
- **Como se usa:** Se instala como libreria Python, se crea una coleccion y se puebla con los triggers al iniciar el servidor

---

### 8. Git — https://git-scm.com
**Funcion:** Control de versiones del codigo.
- Registra cada cambio hecho al proyecto con fecha y descripcion
- Permite subir el codigo a GitHub con el comando `git push`
- **Plan gratuito:** completamente gratuito y open source
- **Version instalada:** 2.53.0 para Windows

---

### RESUMEN DE PLATAFORMAS

| Plataforma | URL | Funcion Principal | Costo |
|---|---|---|---|
| Groq | console.groq.com | LLM — cerebro del bot | Gratis |
| Railway | railway.app | Hosting del backend 24/7 | Gratis |
| AWS S3 | aws.amazon.com | Hosting del frontend publico | Gratis |
| GitHub | github.com | Repositorio del codigo | Gratis |
| PlantUML | plantuml.com | Generacion de diagramas UML | Gratis |
| Kiro | IDE local | Desarrollo del proyecto | Gratis |
| ChromaDB | trychroma.com | Base de datos vectorial | Gratis |
| Git | git-scm.com | Control de versiones | Gratis |

**Costo total de todas las plataformas: $0**

Se construyo un chatbot de ventas completo para Gym CENFE con las siguientes capacidades:

- Atiende **50 casos de uso** diferentes cubriendo todo el ciclo de vida del cliente
- Implementa un **funnel de ventas de 7 etapas** que guia al usuario desde el primer contacto hasta la fidelizacion
- Usa **IA generativa** (Groq/LLaMA 3) para respuestas naturales y personalizadas
- Tiene **busqueda semantica** con ChromaDB para detectar la intencion del usuario
- Responde en **tiempo real** con streaming token por token
- Genera **quick replies dinamicos** coherentes con cada respuesta
- Esta **desplegado en produccion** y accesible desde cualquier dispositivo con internet
- Todo el stack es **100% gratuito**

**Costo total del proyecto: $0**

---

## 19. APLICACIONES INSTALADAS EN LA PC

Todas las aplicaciones instaladas localmente para desarrollar y correr el proyecto.

---

### 1. Python 3.11.9
**Descarga:** https://python.org  
**Funcion:** Lenguaje principal del proyecto. Todo el backend esta escrito en Python — el servidor, la logica del bot, la base de datos vectorial y el servidor MCP.  
**Por que esta version:** Compatible con FastAPI, ChromaDB y Groq. Es la misma version que usa Railway en produccion.  
**Importante en instalacion:** Marcar "Add Python to PATH" para usarlo desde cualquier terminal.  
**Verificacion:** `python --version`

---

### 2. Git 2.53.0
**Descarga:** https://git-scm.com  
**Funcion:** Control de versiones. Guarda el historial de cambios y sube el codigo a GitHub para que Railway lo descargue automaticamente.  
**Comandos usados:**
- `git init` — inicializar repositorio local
- `git add .` — preparar todos los archivos para guardar
- `git commit -m "mensaje"` — guardar cambio con descripcion
- `git remote add origin URL` — conectar con GitHub
- `git push` — subir codigo a GitHub  
**Verificacion:** `git --version`

---

### 3. Kiro (IDE)
**Funcion:** Editor de codigo donde se desarrollo todo el proyecto.  
**Usos en el proyecto:**
- Escribir y editar archivos Python, HTML, JSON
- Terminal integrada para ejecutar comandos
- Configuracion del servidor MCP para diagramas
- Asistencia con IA durante el desarrollo

---

### 4. Librerias Python instaladas via pip

Comando de instalacion:
```bash
pip install -r backend/requirements.txt
```

| Libreria | Version | Funcion |
|---|---|---|
| **fastapi** | 0.135.3 | Framework para crear los endpoints de la API REST |
| **uvicorn** | 0.29.0 | Servidor que corre FastAPI y escucha peticiones |
| **chromadb** | 0.5.0 | Base de datos vectorial para busqueda semantica |
| **groq** | 0.9.0 | Cliente oficial para llamar al LLM de Groq |
| **python-dotenv** | 1.0.1 | Leer API keys desde el archivo .env |
| **pydantic** | 2.12.5 | Validar datos que entran y salen de la API |
| **httpx** | 0.27.0 | Cliente HTTP para llamadas externas |
| **plantuml** | 0.3.0 | Generar diagramas PlantUML desde Python |
| **mcp** | 1.0.0 | Protocolo para integracion con Kiro |
| **numpy** | 1.26.4 | Operaciones matematicas para ChromaDB |
| **onnxruntime** | 1.24.4 | Motor para ejecutar el modelo de embeddings ONNX |

**FastAPI** — crea los endpoints `/chat/stream`, `/reset`, `/health`. Maneja las peticiones del frontend y soporta streaming SSE nativo.

**Uvicorn** — servidor que "corre" FastAPI en el puerto 8000. Con `--reload` detecta cambios y reinicia automaticamente. En Railway se inicia con el Procfile.

**ChromaDB** — almacena 476 triggers como vectores. Usa ONNX MiniLM para convertir texto a numeros. Guarda datos en SQLite local. Busca por similitud coseno.

**Groq SDK** — libreria oficial para comunicarse con Groq. Soporta streaming nativo con `stream=True`. Maneja la autenticacion con la API Key automaticamente.

**python-dotenv** — lee el archivo `.env` y carga GROQ_API_KEY, GROQ_MODEL, etc. Evita escribir keys directamente en el codigo. El .env nunca se sube a GitHub.

**ONNX Runtime** — ejecuta el modelo de embeddings MiniLM localmente sin internet. Pesa ~50MB vs 2GB de PyTorch. Incluido automaticamente con ChromaDB.

---

### 5. Entorno Virtual Python (venv)
**Funcion:** Aislamiento de dependencias del proyecto.  
**Por que es importante:** Las librerias de CENFE FitBot no afectan otros proyectos Python en la misma computadora.  
**Ubicacion:** `cenfe-chatbot/venv/`  
**Creacion:** `python -m venv venv`  
**Activacion:** `venv\Scripts\activate`  
**Indicador:** El prompt muestra `(venv)` cuando esta activo.

---

### RESUMEN DE APLICACIONES

| Aplicacion | Version | Tipo | Funcion |
|---|---|---|---|
| Python | 3.11.9 | Lenguaje | Backend del bot |
| Git | 2.53.0 | Herramienta | Subir codigo a GitHub |
| Kiro | - | IDE | Desarrollo del proyecto |
| FastAPI | 0.135.3 | Libreria | API REST del servidor |
| Uvicorn | 0.29.0 | Libreria | Servidor web |
| ChromaDB | 0.5.0 | Libreria | Base de datos vectorial |
| Groq SDK | 0.9.0 | Libreria | Cliente del LLM |
| python-dotenv | 1.0.1 | Libreria | Variables de entorno |
| ONNX Runtime | 1.24.4 | Libreria | Modelo de embeddings |
| numpy | 1.26.4 | Libreria | Matematicas vectoriales |
| pydantic | 2.12.5 | Libreria | Validacion de datos |

**Costo total de instalaciones: $0**
