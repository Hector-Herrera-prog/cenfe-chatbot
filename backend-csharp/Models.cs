namespace CenfeFitBot;

public record ChatRequest(string? SessionId, string Message);

public record ChatResponse(
    string SessionId,
    string Response,
    List<string> QuickReplies,
    string Intent,
    double Confidence
);

public record UserProfile
{
    public string? Objetivo { get; set; }
    public string? Experiencia { get; set; }
    public int? DiasDisponibles { get; set; }
    public string? Lesion { get; set; }
    public string EtapaFunnel { get; set; } = "atraccion";
    public bool EsMiembro { get; set; } = false;
    public int MensajesCount { get; set; } = 0;
}

public record VectorEntry(string Text, string CaseId, string Intent, string ResponseKey);
