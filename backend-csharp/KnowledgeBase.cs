namespace CenfeFitBot;

public static class KnowledgeBase
{
    public static void Seed(VectorStore store)
    {
        var cases = new List<(string text, string caseId, string intent, string responseKey)>
        {
            // BLOQUE A - Adquisicion
            ("quiero inscribirme al gym","inscripcion","inscripcion_nueva","quiz_perfil"),
            ("como me registro en el gym","inscripcion","inscripcion_nueva","quiz_perfil"),
            ("quiero una membresia","inscripcion","inscripcion_nueva","quiz_perfil"),
            ("quiero empezar en el gym","inscripcion","inscripcion_nueva","quiz_perfil"),
            ("cuanto cuesta la membresia","precio","consulta_precio","presentar_valor"),
            ("cual es el precio del gym","precio","consulta_precio","presentar_valor"),
            ("cuanto cobran por mes","precio","consulta_precio","presentar_valor"),
            ("quiero saber los precios","precio","consulta_precio","presentar_valor"),
            ("soy principiante nunca he ido al gym","principiante","principiante_nuevo","onboarding"),
            ("no tengo experiencia en el gym","principiante","principiante_nuevo","onboarding"),
            ("es mi primera vez en un gym","principiante","principiante_nuevo","onboarding"),
            ("que horarios tienen","horarios","info_logistica","info_horarios"),
            ("a que hora abren el gym","horarios","info_logistica","info_horarios"),
            ("donde estan ubicados","horarios","info_logistica","info_horarios"),
            ("quiero tomar clases de spinning","clases","reserva_clase","urgencia_cupo"),
            ("tienen clases grupales","clases","reserva_clase","urgencia_cupo"),
            ("quiero ir con mi pareja","grupal","venta_grupal","paquete_grupal"),
            ("somos dos personas queremos inscribirnos","grupal","venta_grupal","paquete_grupal"),
            ("quiero volver al gym deje de ir","reactivacion","reactivacion","bienvenida_reactivacion"),
            ("tenia membresia antes quiero reactivar","reactivacion","reactivacion","bienvenida_reactivacion"),
            // BLOQUE B - Servicio
            ("quiero congelar mi membresia","congelacion","congelacion_membresia","proceso_congelacion"),
            ("me voy de viaje puedo pausar","congelacion","congelacion_membresia","proceso_congelacion"),
            ("que debo comer para bajar de peso","nutricion","crosssell_nutricion","oferta_nutricion"),
            ("necesito un plan nutricional","nutricion","crosssell_nutricion","oferta_nutricion"),
            ("tengo una queja del servicio","queja","gestion_queja","atencion_queja"),
            ("una maquina esta rota","queja","gestion_queja","atencion_queja"),
            // BLOQUE D - Psicologia
            ("me da pena ir al gym","pena","inseguridad_social","ambiente_inclusivo"),
            ("me da verguenza no saber usar las maquinas","pena","inseguridad_social","ambiente_inclusivo"),
            ("no tengo tiempo para ir al gym","tiempo","objecion_tiempo","rutinas_express"),
            ("estoy muy ocupado trabajo mucho","tiempo","objecion_tiempo","rutinas_express"),
            ("siempre abandono el gym no tengo disciplina","abandono","falta_disciplina","accountability"),
            ("hoy me da flojera no quiero ir","flojera","baja_motivacion","boost_motivacion"),
            ("no veo resultados en el gym","resultados","frustracion_resultados","diagnostico"),
            // BLOQUE F - Entrenamiento
            ("quiero una rutina de ejercicios","rutina","rutina_personalizada","generar_rutina"),
            ("dame un plan de entrenamiento","rutina","rutina_personalizada","generar_rutina"),
            ("quiero bajar de peso con ejercicio","bajar_peso","rutina_personalizada","generar_rutina"),
            ("quiero ganar musculo","musculo","rutina_personalizada","generar_rutina"),
            ("ejercicios que puedo hacer en casa","casa","rutina_casa","rutina_sin_equipo"),
            // BLOQUE G - Nutricion
            ("cuantas calorias necesito al dia","calorias","control_calorias","calculo_calorias"),
            ("no me gusta el pollo que puedo comer","sustituciones","sustitucion_alimentos","alternativas"),
            ("soy vegetariano que como","sustituciones","sustitucion_alimentos","alternativas"),
            // BLOQUE H - Salud
            ("me duele la rodilla puedo entrenar","lesion","lesion_especifica","protocolo_lesion"),
            ("tengo dolor de espalda","lesion","lesion_especifica","protocolo_lesion"),
            ("tengo diabetes puedo hacer ejercicio","enfermedad","condicion_medica","adaptacion_medica"),
            ("tengo presion alta es seguro entrenar","enfermedad","condicion_medica","adaptacion_medica"),
            // BLOQUE I - Engagement
            ("cuantos dias llevo de racha","racha","gamificacion_racha","mostrar_racha"),
            ("quiero participar en un reto","reto","reto_mensual","info_reto"),
            ("ver el ranking del gym","ranking","ranking_usuarios","mostrar_ranking"),
            // BLOQUE M - Ventas
            ("quiero mejorar mi plan de membresia","upsell","upsell_plan","comparativa_planes"),
            ("hay alguna oferta o descuento","oferta","oferta_personalizada","oferta_perfil"),
            // BLOQUE N - IA
            ("quiero cancelar mi membresia","cancelar","riesgo_abandono","retencion_proactiva"),
            ("estoy pensando en darme de baja","cancelar","riesgo_abandono","retencion_proactiva"),
        };

        foreach (var (text, caseId, intent, responseKey) in cases)
            store.Add(new VectorEntry(text, caseId, intent, responseKey));
    }
}
