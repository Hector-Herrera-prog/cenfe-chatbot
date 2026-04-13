#!/usr/bin/env python3
"""
MCP Server para generar diagramas de casos de uso CENFE
Usa PlantUML (gratuito) para generar los diagramas
"""
import json
import sys
import httpx
import base64
import zlib
from typing import Any

# Protocolo MCP simplificado sobre stdio
def send_response(id: Any, result: Any):
    response = {"jsonrpc": "2.0", "id": id, "result": result}
    print(json.dumps(response), flush=True)

def send_error(id: Any, code: int, message: str):
    response = {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}
    print(json.dumps(response), flush=True)

def plantuml_encode(text: str) -> str:
    """Codificar texto PlantUML para URL"""
    data = text.encode("utf-8")
    compressed = zlib.compress(data)[2:-4]
    
    # Codificacion especial de PlantUML
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    b64 = base64.b64encode(compressed).decode("ascii")
    
    result = ""
    for char in b64:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            idx = ord(char) - ord("A") if char.isupper() else ord(char) - ord("a") + 26
            result += alphabet[idx % len(alphabet)]
        elif char in "0123456789":
            result += char
        elif char == "+":
            result += "-"
        elif char == "/":
            result += "_"
        else:
            result += char
    return result

def generate_use_case_diagram(block: str = "all") -> dict:
    """Generar diagrama de casos de uso para CENFE"""
    
    diagrams = {
        "all": generate_full_diagram(),
        "adquisicion": generate_block_a(),
        "servicio": generate_block_b(),
        "retencion": generate_block_c(),
        "psicologia": generate_block_d(),
        "entrenamiento": generate_block_f(),
        "nutricion": generate_block_g(),
        "salud": generate_block_h(),
        "engagement": generate_block_i(),
        "ventas_avanzadas": generate_block_m(),
    }
    
    uml = diagrams.get(block, diagrams["all"])
    encoded = plantuml_encode(uml)
    url = f"https://www.plantuml.com/plantuml/png/{encoded}"
    
    return {
        "diagram_url": url,
        "plantuml_code": uml,
        "block": block,
        "description": f"Diagrama de casos de uso CENFE - Bloque: {block}"
    }

def generate_full_diagram() -> str:
    return """
@startuml CENFE_Full_Use_Cases
!theme cerulean
title Gym CENFE - Sistema Completo de Casos de Uso

left to right direction
skinparam actorStyle awesome
skinparam packageStyle rectangle

actor "Usuario Nuevo" as UN
actor "Miembro Activo" as MA
actor "Miembro Inactivo" as MI
actor "FitBot IA" as BOT

rectangle "CENFE FitBot System" {
  package "Adquisicion" {
    usecase "UC01 Onboarding Principiante" as UC01
    usecase "UC02 Atleta Estancado" as UC02
    usecase "UC03 Reactivacion" as UC03
    usecase "UC04 Consulta Precio" as UC04
    usecase "UC05 Miedo a Pesas" as UC05
    usecase "UC06 Horarios/Sucursales" as UC06
    usecase "UC07 Reserva Clases" as UC07
    usecase "UC08 Venta Grupal" as UC08
    usecase "UC09 Recuperar Pago" as UC09
  }
  package "Servicio" {
    usecase "UC10 Congelacion" as UC10
    usecase "UC11 Cross-sell Nutricion" as UC11
    usecase "UC12 Gestion Quejas" as UC12
  }
  package "Retencion" {
    usecase "UC13 Logros/Gamificacion" as UC13
    usecase "UC14 Encuesta Calidad" as UC14
    usecase "UC15 Programa Referidos" as UC15
    usecase "UC16 Reporte Progreso" as UC16
  }
  package "Psicologia" {
    usecase "UC17 Sin Tiempo" as UC17
    usecase "UC18 Pena/Inseguridad" as UC18
    usecase "UC19 Abandono Recurrente" as UC19
    usecase "UC20 Sin Resultados" as UC20
    usecase "UC21 Baja Motivacion" as UC21
  }
  package "Entrenamiento" {
    usecase "UC25 Rutina Personalizada" as UC25
    usecase "UC26 Ajuste Rutina" as UC26
    usecase "UC27 Rutina en Casa" as UC27
  }
  package "Nutricion" {
    usecase "UC28 Plan Semanal" as UC28
    usecase "UC29 Sustituciones" as UC29
    usecase "UC30 Control Calorias" as UC30
  }
  package "Salud" {
    usecase "UC31 Lesiones" as UC31
    usecase "UC32 Enfermedades" as UC32
    usecase "UC33 Rehabilitacion" as UC33
  }
  package "Engagement" {
    usecase "UC34 Recordatorios" as UC34
    usecase "UC35 Rachas/Streaks" as UC35
    usecase "UC36 Retos Mensuales" as UC36
    usecase "UC37 Ranking" as UC37
  }
  package "IA Avanzada" {
    usecase "UC48 Prediccion Abandono" as UC48
    usecase "UC49 Coaching IA" as UC49
    usecase "UC50 Ajuste Objetivos" as UC50
  }
}

UN --> UC01
UN --> UC04
UN --> UC05
UN --> UC06
UN --> UC07
UN --> UC08
MA --> UC10
MA --> UC11
MA --> UC13
MA --> UC14
MA --> UC15
MA --> UC16
MA --> UC17
MA --> UC25
MA --> UC28
MA --> UC34
MA --> UC35
MA --> UC36
MI --> UC03
MI --> UC09
MI --> UC48
BOT --> UC49
BOT --> UC50
BOT --> UC48

@enduml
"""

def generate_block_a() -> str:
    return """
@startuml CENFE_Block_A
!theme cerulean
title CENFE - Bloque A: Adquisicion (Ventas)

left to right direction
actor "Prospecto" as P
actor "FitBot" as BOT

rectangle "Adquisicion" {
  usecase "Onboarding Principiante" as UC01
  usecase "Atleta Estancado" as UC02
  usecase "Reactivacion Desertor" as UC03
  usecase "Consulta de Precio" as UC04
  usecase "Miedo a las Pesas" as UC05
  usecase "Horarios y Sucursales" as UC06
  usecase "Clases con Cupo Limitado" as UC07
  usecase "Venta en Pareja/Grupo" as UC08
  usecase "Recuperacion Pago Incompleto" as UC09
}

P --> UC01 : "Soy principiante"
P --> UC02 : "Estoy estancado"
P --> UC03 : "Quiero volver"
P --> UC04 : "Cuanto cuesta?"
P --> UC05 : "Me voy a poner grande?"
P --> UC06 : "Que horarios tienen?"
P --> UC07 : "Quiero reservar clase"
P --> UC08 : "Somos dos personas"
P --> UC09 : "No termine de pagar"
BOT --> UC01
BOT --> UC04
BOT --> UC09

@enduml
"""

def generate_block_b() -> str:
    return """
@startuml CENFE_Block_B
!theme cerulean
title CENFE - Bloque B: Servicio y Soporte

left to right direction
actor "Miembro" as M
actor "FitBot" as BOT

rectangle "Servicio" {
  usecase "Congelacion de Membresia" as UC10
  usecase "Cross-sell Nutricion" as UC11
  usecase "Gestion de Quejas" as UC12
}

M --> UC10 : "Necesito pausar"
M --> UC11 : "Quiero mejorar dieta"
M --> UC12 : "Tengo un problema"
BOT --> UC11 : "Oferta proactiva"
BOT --> UC12 : "Escalacion rapida"

@enduml
"""

def generate_block_f() -> str:
    return """
@startuml CENFE_Block_F
!theme cerulean
title CENFE - Bloque F: Entrenamiento Personalizado

left to right direction
actor "Miembro" as M
actor "FitBot IA" as BOT

rectangle "Entrenamiento" {
  usecase "Rutina Personalizada" as UC25
  usecase "Ajuste de Rutina" as UC26
  usecase "Rutina en Casa" as UC27
  usecase "Primer Dia en Gym" as UC22
  usecase "Tour Virtual" as UC23
  usecase "Explicacion Maquinas" as UC24
}

M --> UC25 : "Quiero mi rutina"
M --> UC26 : "Ya avance mucho"
M --> UC27 : "No puedo ir hoy"
M --> UC22 : "Es mi primer dia"
M --> UC23 : "Como es el gym?"
M --> UC24 : "Como uso esto?"
BOT --> UC25 : "Genera rutina"
BOT --> UC26 : "Ajusta progresion"

@enduml
"""

def generate_block_g() -> str:
    return """
@startuml CENFE_Block_G
!theme cerulean
title CENFE - Bloque G: Nutricion Avanzada

left to right direction
actor "Miembro" as M
actor "FitBot IA" as BOT

rectangle "Nutricion" {
  usecase "Plan Semanal Automatico" as UC28
  usecase "Sustituciones de Alimentos" as UC29
  usecase "Control de Calorias" as UC30
}

M --> UC28 : "Que como esta semana?"
M --> UC29 : "No me gusta el pollo"
M --> UC30 : "Cuantas calorias necesito?"
BOT --> UC28 : "Genera menu"
BOT --> UC29 : "Sugiere alternativas"
BOT --> UC30 : "Calcula TDEE"

@enduml
"""

def generate_block_h() -> str:
    return """
@startuml CENFE_Block_H
!theme cerulean
title CENFE - Bloque H: Salud y Rehabilitacion

left to right direction
actor "Miembro" as M
actor "Coach Medico" as CM

rectangle "Salud" {
  usecase "Protocolo Lesiones" as UC31
  usecase "Adaptacion Enfermedades" as UC32
  usecase "Programa Rehabilitacion" as UC33
}

M --> UC31 : "Me duele la rodilla"
M --> UC32 : "Tengo diabetes"
M --> UC33 : "Tuve una cirugia"
CM --> UC31
CM --> UC32
CM --> UC33

@enduml
"""

def generate_block_i() -> str:
    return """
@startuml CENFE_Block_I
!theme cerulean
title CENFE - Bloque I: Engagement y Gamificacion

left to right direction
actor "Miembro" as M
actor "FitBot IA" as BOT

rectangle "Engagement" {
  usecase "Recordatorios Inteligentes" as UC34
  usecase "Rachas (Streaks)" as UC35
  usecase "Retos Mensuales" as UC36
  usecase "Ranking de Usuarios" as UC37
  usecase "Felicitacion Logros" as UC13
}

M --> UC34 : "Recordarme entrenar"
M --> UC35 : "Ver mi racha"
M --> UC36 : "Unirme al reto"
M --> UC37 : "Ver ranking"
BOT --> UC34 : "Envia recordatorio"
BOT --> UC35 : "Actualiza racha"
BOT --> UC13 : "Celebra logro"

@enduml
"""

def generate_block_m() -> str:
    return """
@startuml CENFE_Block_M
!theme cerulean
title CENFE - Bloque M: Ventas Avanzadas e IA

left to right direction
actor "Miembro" as M
actor "FitBot IA" as BOT

rectangle "Ventas Avanzadas" {
  usecase "Upsell Automatico" as UC45
  usecase "Ofertas Personalizadas" as UC46
  usecase "Urgencia Dinamica" as UC47
  usecase "Prediccion Abandono" as UC48
  usecase "Coaching IA" as UC49
  usecase "Ajuste Objetivos" as UC50
}

M --> UC45 : "Quiero mejor plan"
M --> UC46 : "Hay ofertas?"
M --> UC49 : "Quiero coaching"
M --> UC50 : "Cambiar mi objetivo"
BOT --> UC45 : "Detecta oportunidad"
BOT --> UC46 : "Oferta segun perfil"
BOT --> UC47 : "Crea urgencia"
BOT --> UC48 : "Detecta riesgo"

@enduml
"""

def handle_request(request: dict):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})
    
    if method == "initialize":
        send_response(req_id, {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "cenfe-diagrams-mcp", "version": "1.0.0"}
        })
    
    elif method == "tools/list":
        send_response(req_id, {
            "tools": [
                {
                    "name": "generate_use_case_diagram",
                    "description": "Genera diagramas de casos de uso para el sistema CENFE FitBot usando PlantUML",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "block": {
                                "type": "string",
                                "description": "Bloque a diagramar",
                                "enum": ["all", "adquisicion", "servicio", "retencion", "psicologia", "entrenamiento", "nutricion", "salud", "engagement", "ventas_avanzadas"]
                            }
                        },
                        "required": []
                    }
                },
                {
                    "name": "list_use_cases",
                    "description": "Lista todos los casos de uso del sistema CENFE",
                    "inputSchema": {"type": "object", "properties": {}}
                }
            ]
        })
    
    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        
        if tool_name == "generate_use_case_diagram":
            block = tool_args.get("block", "all")
            result = generate_use_case_diagram(block)
            send_response(req_id, {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(result, indent=2, ensure_ascii=False)
                    }
                ]
            })
        
        elif tool_name == "list_use_cases":
            use_cases = {
                "total": 50,
                "bloques": {
                    "A_Adquisicion": ["UC01-Principiante", "UC02-Atleta Estancado", "UC03-Reactivacion", "UC04-Precio", "UC05-Miedo Pesas", "UC06-Horarios", "UC07-Clases", "UC08-Grupal", "UC09-Pago Incompleto"],
                    "B_Servicio": ["UC10-Congelacion", "UC11-Nutricion CrossSell", "UC12-Quejas"],
                    "C_Retencion": ["UC13-Logros", "UC14-Encuesta", "UC15-Referidos", "UC16-Progreso"],
                    "D_Psicologia": ["UC17-Sin Tiempo", "UC18-Pena", "UC19-Abandono", "UC20-Sin Resultados", "UC21-Flojera"],
                    "E_Onboarding": ["UC22-Primer Dia", "UC23-Tour Virtual", "UC24-Maquinas"],
                    "F_Entrenamiento": ["UC25-Rutina", "UC26-Ajuste", "UC27-Casa"],
                    "G_Nutricion": ["UC28-Plan Semanal", "UC29-Sustituciones", "UC30-Calorias"],
                    "H_Salud": ["UC31-Lesiones", "UC32-Enfermedades", "UC33-Rehabilitacion"],
                    "I_Engagement": ["UC34-Recordatorios", "UC35-Rachas", "UC36-Retos", "UC37-Ranking"],
                    "J_Personalizacion": ["UC38-Recomendacion Plan", "UC39-Adaptacion Tono"],
                    "K_Admin": ["UC40-QR", "UC41-Historial", "UC42-Pagos"],
                    "L_Social": ["UC43-Companeros", "UC44-Eventos"],
                    "M_Ventas_Avanzadas": ["UC45-Upsell", "UC46-Ofertas", "UC47-Urgencia"],
                    "N_IA_Avanzada": ["UC48-Prediccion Abandono", "UC49-Coaching IA", "UC50-Ajuste Objetivos"]
                }
            }
            send_response(req_id, {
                "content": [{"type": "text", "text": json.dumps(use_cases, indent=2, ensure_ascii=False)}]
            })
        else:
            send_error(req_id, -32601, f"Tool not found: {tool_name}")
    
    elif method == "notifications/initialized":
        pass  # No response needed
    
    else:
        send_error(req_id, -32601, f"Method not found: {method}")

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            handle_request(request)
        except json.JSONDecodeError as e:
            send_error(None, -32700, f"Parse error: {e}")
        except Exception as e:
            send_error(None, -32603, f"Internal error: {e}")

if __name__ == "__main__":
    main()
