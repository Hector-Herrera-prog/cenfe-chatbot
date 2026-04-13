# Base de conocimiento CENFE - 50 casos de uso
CENFE_INFO = {
    "nombre": "Gym CENFE",
    "slogan": "Tu mejor version empieza aqui",
    "planes": {
        "basico": {"nombre": "Plan Basico", "precio": "$299/mes", "incluye": ["Acceso a maquinas", "Vestidores", "Casillero"]},
        "welcome": {"nombre": "Plan Welcome", "precio": "$399/mes", "incluye": ["Induccion con entrenador", "Tour instalaciones", "App con videos", "Grupo principiantes"]},
        "premium": {"nombre": "Plan Premium", "precio": "$599/mes", "incluye": ["Todo lo anterior", "Clases grupales ilimitadas", "Evaluacion fisica mensual", "Nutricion basica"]},
        "elite": {"nombre": "Plan Elite", "precio": "$899/mes", "incluye": ["Todo Premium", "Entrenador personal 2x semana", "Plan nutricional personalizado", "Acceso multiclub"]}
    },
    "horarios": "Lunes a Viernes 5am-11pm | Sabado 6am-9pm | Domingo 7am-6pm",
    "sucursales": ["CENFE Norte", "CENFE Sur", "CENFE Centro"],
    "clase_prueba": "GRATIS para nuevos miembros",
    "congelacion": "Hasta 3 meses por viaje o motivos medicos",
    "referidos": "1 mes gratis por cada amigo que se inscriba"
}

USE_CASES = {
    # BLOQUE A: ADQUISICION
    "inscripcion_nueva": {
        "triggers": [
            "quiero inscribirme", "quiero registrarme", "quiero unirme", "como me inscribo",
            "quiero ser miembro", "quiero una membresia", "quiero empezar", "como me registro",
            "quiero entrar al gym", "quiero ir al gym", "quiero comenzar", "me quiero inscribir",
            "como me uno", "quiero comprar membresia", "quiero contratar", "informacion para inscribirme"
        ],
        "intent": "inscripcion_nueva",
        "response_key": "quiz_perfil"
    },
    "principiante_nuevo": {
        "triggers": [
            "no se usar las maquinas", "nunca he ido al gym", "empezar desde cero", "soy principiante",
            "no se nada de gym", "es mi primera vez", "nunca he entrenado", "no tengo experiencia",
            "soy nuevo en esto", "no se por donde empezar", "me da miedo no saber",
            "nunca he levantado pesas", "no se hacer ejercicio", "quiero empezar pero no se como"
        ],
        "intent": "nuevo_miembro_principiante",
        "response_key": "onboarding_principiante"
    },
    "atleta_estancado": {
        "triggers": [
            "no veo resultados", "estoy estancado", "no avanzo", "llegue a una meseta",
            "siempre peso lo mismo", "no mejoro", "llevo meses sin cambios", "no progreso",
            "hago ejercicio pero no cambia nada", "ya no bajo de peso", "ya no subo musculo",
            "mis marcas no mejoran", "siento que no avanzo", "estoy en un plateau"
        ],
        "intent": "atleta_avanzado_estancado",
        "response_key": "reto_avanzado"
    },
    "desertor_reactivacion": {
        "triggers": [
            "ya fui antes al gym", "tenia membresia antes", "deje de ir", "quiero volver",
            "estuve inscrito", "me di de baja", "cancele mi membresia", "quiero reactivar",
            "antes iba pero pare", "volvi a empezar", "quiero retomar", "regrese al gym",
            "estuve un tiempo sin ir", "quiero reinscribirme"
        ],
        "intent": "reactivacion",
        "response_key": "bienvenida_reactivacion"
    },
    "consulta_precio": {
        "triggers": [
            "cuanto cuesta", "cual es el precio", "cuanto cobran", "cuanto es la mensualidad",
            "cuanto vale", "que precio tiene", "cuanto sale", "precio de la membresia",
            "tarifas", "costo mensual", "cuanto hay que pagar", "que planes tienen",
            "cuanto es la inscripcion", "tienen algun plan economico", "precios y planes",
            "quiero saber precios", "informacion de precios", "ver precios"
        ],
        "intent": "consulta_precio",
        "response_key": "presentar_valor_antes_precio"
    },
    "miedo_pesas": {
        "triggers": [
            "me voy a poner muy grande", "no quiero ponerme musculosa", "no quiero volumen",
            "solo quiero tonificar", "tengo miedo de las pesas", "las pesas me ponen grande",
            "no quiero parecer culturista", "solo quiero definir", "quiero estar delgada no musculosa",
            "el gym me va a poner enorme", "no quiero masa muscular"
        ],
        "intent": "miedo_hipertrofia",
        "response_key": "educacion_tonificacion"
    },
    "horarios_sucursales": {
        "triggers": [
            "que horarios tienen", "a que hora abren", "a que hora cierran", "cuando abren",
            "horario del gym", "donde estan ubicados", "cual es la direccion", "sucursales",
            "tienen sucursal cerca", "donde queda el gym", "ubicacion", "como llego",
            "abren los domingos", "abren temprano", "cierran tarde"
        ],
        "intent": "info_logistica",
        "response_key": "info_horarios"
    },
    "clases_cupo": {
        "triggers": [
            "quiero tomar una clase", "tienen clases grupales", "clases de spinning",
            "clases de zumba", "clases de yoga", "clases de pilates", "quiero reservar una clase",
            "como reservo", "hay cupo en las clases", "que clases ofrecen", "clases disponibles",
            "horario de clases", "quiero una clase grupal", "clases de baile"
        ],
        "intent": "reserva_clase",
        "response_key": "urgencia_cupo"
    },
    "pareja_grupo": {
        "triggers": [
            "quiero ir con mi pareja", "vamos a ir con mi amigo", "somos dos personas",
            "quiero inscribir a mi familia", "hay descuento para grupos", "membresia familiar",
            "plan para dos", "mi novio y yo queremos inscribirnos", "somos varios amigos",
            "descuento por traer a alguien", "plan grupal", "inscripcion para pareja"
        ],
        "intent": "venta_grupal",
        "response_key": "paquete_grupal"
    },
    "pago_incompleto": {
        "triggers": [
            "no termine de pagar", "deje el registro a medias", "no complete mi inscripcion",
            "empece a registrarme pero no termine", "quede a medias en el pago",
            "tuve un problema al pagar", "no me dejo completar el pago"
        ],
        "intent": "recuperacion_pago",
        "response_key": "recuperar_lead"
    },
    # BLOQUE B: SERVICIO
    "congelacion": {
        "triggers": [
            "quiero congelar mi membresia", "puedo pausar mi membresia", "me voy de viaje",
            "voy a salir de vacaciones", "no puedo ir al gym por un tiempo", "quiero suspender",
            "como se congela la membresia", "puedo pausar", "voy a estar fuera",
            "tuve un accidente", "estoy enfermo", "motivos personales no puedo ir"
        ],
        "intent": "congelacion_membresia",
        "response_key": "proceso_congelacion"
    },
    "nutricion_crosssell": {
        "triggers": [
            "que debo comer", "como debo alimentarme", "necesito una dieta", "quiero mejorar mi nutricion",
            "que como para bajar de peso", "que como para ganar musculo", "plan de alimentacion",
            "tienen nutriologo", "servicio de nutricion", "quiero un plan nutricional"
        ],
        "intent": "crosssell_nutricion",
        "response_key": "oferta_nutricion"
    },
    "queja": {
        "triggers": [
            "tengo una queja", "quiero reportar un problema", "una maquina esta rota",
            "el gym esta sucio", "mal servicio", "no me atendieron bien", "tuve un problema",
            "quiero hablar con el gerente", "algo no funciona", "estoy molesto con el servicio"
        ],
        "intent": "gestion_queja",
        "response_key": "atencion_queja"
    },
    # BLOQUE C: RETENCION
    "logro_felicitacion": {
        "triggers": [
            "logre mi meta", "baje de peso", "ya puedo hacer mas repeticiones", "cumpli un mes",
            "alcance mi objetivo", "lo logre", "estoy muy contento con mis resultados",
            "perdi kilos", "gane musculo", "mejore mis marcas", "primer mes completado"
        ],
        "intent": "celebrar_logro",
        "response_key": "felicitacion_gamificacion"
    },
    "encuesta": {
        "triggers": [
            "quiero dar mi opinion", "como califico el servicio", "encuesta de satisfaccion",
            "quiero dar feedback", "que opinion les doy", "como evaluo el gym"
        ],
        "intent": "encuesta_calidad",
        "response_key": "solicitar_feedback"
    },
    "referidos": {
        "triggers": [
            "quiero referir a alguien", "puedo traer a un amigo", "hay descuento por referidos",
            "programa de referidos", "traer a alguien y ganar algo", "recomendar el gym",
            "mi amigo quiere inscribirse", "como funciona el programa de referidos"
        ],
        "intent": "programa_referidos",
        "response_key": "info_referidos"
    },
    "progreso": {
        "triggers": [
            "quiero ver mi progreso", "cuanto he avanzado", "mis medidas", "evaluacion fisica",
            "quiero saber mis resultados", "como voy con mis metas", "historial de progreso",
            "quiero una evaluacion", "medir mi avance"
        ],
        "intent": "reporte_progreso",
        "response_key": "evaluacion_fisica"
    },
    # BLOQUE D: PSICOLOGIA
    "no_tiempo": {
        "triggers": [
            "no tengo tiempo para ir al gym", "trabajo mucho", "estoy muy ocupado",
            "no puedo ir seguido", "solo tengo poco tiempo", "tengo agenda muy llena",
            "entre semana no puedo", "no me alcanza el tiempo", "muy poco tiempo libre"
        ],
        "intent": "objecion_tiempo",
        "response_key": "rutinas_express"
    },
    "pena_gym": {
        "triggers": [
            "me da pena ir al gym", "me da verguenza", "siento que me van a ver",
            "me juzgan en el gym", "me siento inseguro", "soy timido", "me da miedo que me vean",
            "no me siento comodo", "siento que todos me miran", "me da pena no saber"
        ],
        "intent": "inseguridad_social",
        "response_key": "ambiente_inclusivo"
    },
    "siempre_abandona": {
        "triggers": [
            "siempre abandono el gym", "nunca termino lo que empiezo", "no tengo disciplina",
            "empiezo y luego dejo", "ya intente varias veces", "no me dura la motivacion",
            "siempre me rindo", "no soy constante", "me cuesta mantener el habito"
        ],
        "intent": "falta_disciplina",
        "response_key": "sistema_accountability"
    },
    "no_resultados": {
        "triggers": [
            "no veo ningun cambio", "el gym no me funciona", "perdi el tiempo yendo",
            "no sirve para mi", "llevo tiempo y nada", "no noto diferencia",
            "me esfuerzo y no pasa nada", "siento que no vale la pena"
        ],
        "intent": "frustracion_resultados",
        "response_key": "diagnostico_personalizado"
    },
    "flojera": {
        "triggers": [
            "hoy me da flojera", "no tengo ganas de ir", "estoy muy cansado",
            "no quiero ir al gym hoy", "sin energia", "desmotivado", "no me provoca ir",
            "me siento flojo", "no tengo motivacion hoy", "me cuesta arrancar"
        ],
        "intent": "baja_motivacion",
        "response_key": "boost_motivacion"
    },
    # BLOQUE E: ONBOARDING
    "primer_dia": {
        "triggers": [
            "que necesito para mi primer dia", "que llevo al gym", "como es el primer dia",
            "que traer al gym", "que ropa usar", "necesito traer algo especial",
            "como prepararme para ir", "que pasa el primer dia"
        ],
        "intent": "onboarding_primer_dia",
        "response_key": "guia_primer_dia"
    },
    "tour_virtual": {
        "triggers": [
            "como son las instalaciones", "que tiene el gym", "pueden darme un tour",
            "quiero conocer el gym", "como se ve el gym", "que areas tienen",
            "tienen alberca", "tienen sauna", "que equipos tienen"
        ],
        "intent": "tour_virtual",
        "response_key": "descripcion_instalaciones"
    },
    "explicacion_maquinas": {
        "triggers": [
            "como uso esta maquina", "para que sirve esta maquina", "como se hace este ejercicio",
            "no se usar la maquina", "explicame como funciona", "ejercicio para piernas",
            "ejercicio para espalda", "como se usa la polea", "como funciona la prensa"
        ],
        "intent": "educacion_maquinas",
        "response_key": "guia_maquinas"
    },
    # BLOQUE F: ENTRENAMIENTO
    "rutina_personalizada": {
        "triggers": [
            "quiero una rutina", "dame un plan de entrenamiento", "que ejercicios hago",
            "como entreno", "rutina para bajar de peso", "rutina para ganar musculo",
            "programa de ejercicios", "que hago en el gym", "rutina para principiantes",
            "diseñame una rutina", "quiero un plan"
        ],
        "intent": "rutina_personalizada",
        "response_key": "generar_rutina"
    },
    "ajuste_rutina": {
        "triggers": [
            "quiero cambiar mi rutina", "ya me aburri de mi rutina", "quiero algo diferente",
            "ya avance mucho con esta rutina", "necesito un nuevo reto", "mi rutina ya es facil",
            "quiero progresar mas", "cambiar el programa"
        ],
        "intent": "ajuste_rutina",
        "response_key": "progresion_rutina"
    },
    "rutina_casa": {
        "triggers": [
            "ejercicios en casa", "no puedo ir al gym hoy", "rutina sin equipo",
            "entreno en casa", "ejercicios sin maquinas", "que hago si no voy al gym",
            "rutina para hacer en casa", "no tengo equipo"
        ],
        "intent": "rutina_casa",
        "response_key": "rutina_sin_equipo"
    },
    # BLOQUE G: NUTRICION AVANZADA
    "plan_semanal": {
        "triggers": [
            "que como esta semana", "menu semanal", "plan de comidas semanal",
            "dieta para la semana", "que debo comer cada dia", "menu de la semana",
            "plan nutricional semanal", "comidas para toda la semana"
        ],
        "intent": "plan_nutricional",
        "response_key": "menu_semanal"
    },
    "sustituciones": {
        "triggers": [
            "no me gusta el pollo", "soy vegetariano", "no como carne", "alternativa al pollo",
            "que puedo comer en lugar de", "sustituir un alimento", "soy vegano",
            "tengo alergia a", "no tolero la lactosa", "no como pescado"
        ],
        "intent": "sustitucion_alimentos",
        "response_key": "alternativas_alimenticias"
    },
    "calorias": {
        "triggers": [
            "cuantas calorias necesito", "como cuento calorias", "deficit calorico",
            "cuantas proteinas necesito", "mis macros", "cuanto debo comer",
            "calcular mis calorias", "cuantas calorias para bajar de peso",
            "superavit calorico", "cuanta proteina comer"
        ],
        "intent": "control_calorias",
        "response_key": "calculo_calorias"
    },
    # BLOQUE H: SALUD
    "lesion": {
        "triggers": [
            "tengo una lesion", "me duele la rodilla", "me duele la espalda",
            "me lastime el hombro", "tengo dolor al entrenar", "me duele cuando hago ejercicio",
            "tengo una molestia", "me lesione", "dolor en el tobillo", "me duele la cadera"
        ],
        "intent": "lesion_especifica",
        "response_key": "protocolo_lesion"
    },
    "enfermedad": {
        "triggers": [
            "tengo diabetes", "tengo presion alta", "tengo hipertension", "tengo una condicion medica",
            "puedo entrenar con diabetes", "es seguro con mi enfermedad", "tengo problemas del corazon",
            "tengo obesidad", "tengo colesterol alto", "tengo una condicion especial"
        ],
        "intent": "condicion_medica",
        "response_key": "adaptacion_medica"
    },
    "rehabilitacion": {
        "triggers": [
            "me opere", "tuve una cirugia", "estoy en rehabilitacion", "me fracture",
            "necesito fisioterapia", "me estoy recuperando de una lesion",
            "puedo entrenar despues de una operacion", "recuperacion post cirugia"
        ],
        "intent": "rehabilitacion",
        "response_key": "programa_rehabilitacion"
    },
    # BLOQUE I: ENGAGEMENT
    "recordatorio": {
        "triggers": [
            "quiero que me recuerden entrenar", "pueden mandarme recordatorios",
            "activar notificaciones", "recordatorio de entrenamiento",
            "que me avisen cuando entrenar", "no quiero olvidar ir al gym"
        ],
        "intent": "recordatorio_entrenamiento",
        "response_key": "activar_recordatorios"
    },
    "racha": {
        "triggers": [
            "cuantos dias llevo seguidos", "mi racha de entrenamiento", "dias consecutivos",
            "ver mi streak", "cuantos dias he ido", "mi racha actual"
        ],
        "intent": "gamificacion_racha",
        "response_key": "mostrar_racha"
    },
    "reto_mensual": {
        "triggers": [
            "hay algun reto", "quiero participar en un reto", "reto del mes",
            "challenge del gym", "competencia interna", "desafio mensual",
            "quiero un reto", "que retos tienen"
        ],
        "intent": "reto_mensual",
        "response_key": "info_reto"
    },
    "ranking": {
        "triggers": [
            "ver el ranking", "quien va primero", "tabla de posiciones",
            "clasificacion de miembros", "top del gym", "quien entrena mas",
            "estoy en el ranking", "mi posicion en el ranking"
        ],
        "intent": "ranking_usuarios",
        "response_key": "mostrar_ranking"
    },
    # BLOQUE J: PERSONALIZACION
    "recomendacion_plan": {
        "triggers": [
            "que plan me recomiendas", "cual plan es mejor para mi", "que membresia me conviene",
            "ayudame a elegir un plan", "no se que plan tomar", "cual es el mejor plan",
            "que plan se adapta a mi", "recomiendame algo"
        ],
        "intent": "recomendacion_plan",
        "response_key": "quiz_perfil"
    },
    # BLOQUE K: ADMIN
    "acceso_qr": {
        "triggers": [
            "como entro al gym", "necesito mi codigo qr", "donde esta mi qr",
            "perdi mi acceso", "no puedo entrar", "codigo de entrada", "mi qr no funciona"
        ],
        "intent": "acceso_qr",
        "response_key": "info_qr"
    },
    "historial_asistencia": {
        "triggers": [
            "cuantas veces he ido al gym", "ver mi historial", "mis visitas",
            "registro de asistencia", "cuantos dias fui este mes", "mi historial de visitas"
        ],
        "intent": "historial_asistencia",
        "response_key": "ver_historial"
    },
    "pago_automatico": {
        "triggers": [
            "pago automatico", "domiciliar mi pago", "cobro automatico",
            "renovacion automatica", "que me cobren automatico", "configurar pago mensual"
        ],
        "intent": "pago_automatico",
        "response_key": "configurar_pago"
    },
    # BLOQUE L: SOCIAL
    "buscar_companero": {
        "triggers": [
            "busco companero de entrenamiento", "quiero entrenar con alguien",
            "workout buddy", "busco pareja de gym", "alguien con quien entrenar",
            "comunidad del gym", "conocer gente en el gym"
        ],
        "intent": "buscar_companero",
        "response_key": "comunidad_cenfe"
    },
    "eventos": {
        "triggers": [
            "hay eventos en el gym", "clases especiales", "eventos del mes",
            "actividades especiales", "maratón de spinning", "clase tematica",
            "que eventos tienen", "proximos eventos"
        ],
        "intent": "eventos_especiales",
        "response_key": "calendario_eventos"
    },
    # BLOQUE M: VENTAS AVANZADAS
    "upsell": {
        "triggers": [
            "quiero mejorar mi plan", "cambiar a un plan mejor", "subir de plan",
            "que incluye el plan premium", "diferencia entre planes", "quiero mas beneficios",
            "vale la pena el plan elite", "comparar planes"
        ],
        "intent": "upsell_plan",
        "response_key": "comparativa_planes"
    },
    "oferta_personalizada": {
        "triggers": [
            "hay alguna oferta", "tienen descuentos", "alguna promocion",
            "precio especial", "descuento disponible", "oferta del mes"
        ],
        "intent": "oferta_personalizada",
        "response_key": "oferta_segun_perfil"
    },
    "urgencia": {
        "triggers": [
            "quedan lugares", "se esta llenando", "ultima oportunidad",
            "solo hoy", "oferta por tiempo limitado", "cupos disponibles"
        ],
        "intent": "urgencia_dinamica",
        "response_key": "crear_urgencia"
    },
    # BLOQUE N: IA AVANZADA
    "prediccion_abandono": {
        "triggers": [
            "creo que voy a dejar el gym", "estoy pensando en cancelar", "no se si seguir",
            "quiero cancelar mi membresia", "ya no quiero ir", "no vale la pena seguir",
            "me quiero dar de baja", "cancelar"
        ],
        "intent": "riesgo_abandono",
        "response_key": "retencion_proactiva"
    },
    "coaching_ia": {
        "triggers": [
            "quiero un coach virtual", "coaching personalizado", "seguimiento personalizado",
            "quiero que me guien", "necesito un entrenador virtual", "asistente de entrenamiento"
        ],
        "intent": "coaching_ia",
        "response_key": "sesion_coaching"
    },
    "ajuste_objetivos": {
        "triggers": [
            "quiero cambiar mi objetivo", "tengo una nueva meta", "quiero algo diferente ahora",
            "mis objetivos cambiaron", "quiero redefinir mis metas", "nuevo objetivo"
        ],
        "intent": "ajuste_objetivos",
        "response_key": "redefinir_objetivos"
    }
}
