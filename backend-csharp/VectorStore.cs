namespace CenfeFitBot;

/// <summary>
/// Búsqueda semántica por Similitud de Cosenos en memoria.
/// Implementa vectores TF-IDF simplificados para español.
/// </summary>
public class VectorStore
{
    private readonly List<(VectorEntry Entry, double[] Vector)> _store = new();

    public void Add(VectorEntry entry)
    {
        var vector = Vectorize(entry.Text);
        _store.Add((entry, vector));
    }

    public VectorEntry? FindBestMatch(string query, out double confidence)
    {
        if (_store.Count == 0) { confidence = 0; return null; }

        var queryVec = Vectorize(query);
        double bestScore = -1;
        VectorEntry? bestEntry = null;

        foreach (var (entry, vec) in _store)
        {
            double score = CosineSimilarity(queryVec, vec);
            if (score > bestScore)
            {
                bestScore = score;
                bestEntry = entry;
            }
        }

        confidence = Math.Round(bestScore, 3);
        return bestScore >= 0.25 ? bestEntry : null;
    }

    // Similitud de Cosenos: cos(θ) = (A·B) / (|A| * |B|)
    private static double CosineSimilarity(double[] a, double[] b)
    {
        if (a.Length != b.Length) return 0;
        double dot = 0, magA = 0, magB = 0;
        for (int i = 0; i < a.Length; i++)
        {
            dot  += a[i] * b[i];
            magA += a[i] * a[i];
            magB += b[i] * b[i];
        }
        double denom = Math.Sqrt(magA) * Math.Sqrt(magB);
        return denom == 0 ? 0 : dot / denom;
    }

    // Vocabulario compartido para todos los vectores
    private static readonly string[] Vocabulary = BuildVocabulary();

    private static double[] Vectorize(string text)
    {
        var words = Normalize(text);
        var vec = new double[Vocabulary.Length];
        for (int i = 0; i < Vocabulary.Length; i++)
            vec[i] = words.Count(w => w == Vocabulary[i]);
        return vec;
    }

    private static string[] Normalize(string text) =>
        text.ToLowerInvariant()
            .Replace("á","a").Replace("é","e").Replace("í","i")
            .Replace("ó","o").Replace("ú","u").Replace("ñ","n")
            .Split(new[]{ ' ', ',', '.', '?', '!', ';', ':' },
                   StringSplitOptions.RemoveEmptyEntries);

    private static string[] BuildVocabulary() => new[]
    {
        // Adquisicion
        "inscribir","inscribirme","registrar","membresia","unirme","empezar","comenzar",
        "precio","costo","cuanto","cobran","mensualidad","tarifa","planes","plan",
        "principiante","nunca","primera","vez","cero","experiencia","nuevo",
        "horario","hora","abren","cierran","sucursal","ubicacion","donde",
        "clase","spinning","zumba","yoga","pilates","reservar","cupo","grupal",
        "pareja","amigo","grupo","familia","descuento","varios",
        "volver","reactivar","regrese","inscrito","antes","deje","cancelar",
        // Psicologia
        "pena","verguenza","miedo","inseguro","timido","juzgan",
        "tiempo","ocupado","trabajo","rapido","express",
        "abandono","disciplina","constante","siempre","dejo",
        "resultados","cambios","funciona","avance","progreso",
        "flojera","cansado","ganas","motivacion","energia",
        // Entrenamiento
        "rutina","ejercicios","programa","entrenamiento","pesas","cardio",
        "bajar","peso","adelgazar","quemar","grasa","perder",
        "ganar","musculo","volumen","masa","hipertrofia",
        "tonificar","definir","marcar","figura",
        "casa","equipo","sin","maquinas",
        // Nutricion
        "comer","dieta","nutricion","alimentacion","comidas","menu","semanal",
        "calorias","proteina","macros","deficit","superavit",
        "vegetariano","vegano","carne","pollo","sustituir","alternativa",
        // Salud
        "lesion","duele","rodilla","espalda","hombro","dolor",
        "diabetes","presion","hipertension","enfermedad","condicion",
        "rehabilitacion","cirugia","operacion","recuperacion",
        // Retencion
        "logre","baje","alcance","meta","objetivo","logro",
        "referir","amigo","traer","referido","recomendar",
        "racha","dias","consecutivos","streak",
        "reto","challenge","competencia","desafio",
        "ranking","posicion","tabla","clasificacion",
        // Admin
        "qr","codigo","acceso","entrada","historial","visitas","asistencia",
        "pago","automatico","cobro","renovacion",
        // Congelacion
        "congelar","pausar","viaje","vacaciones","suspender",
        // Queja
        "queja","problema","rota","sucio","servicio","gerente"
    };
}
