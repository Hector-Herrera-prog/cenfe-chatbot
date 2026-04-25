using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Text.Json;

namespace CenfeFitBot;

[ApiController]
[Route("[controller]")]
public class ChatController : ControllerBase
{
    private readonly GroqService _groq;
    private readonly VectorStore _vectors;
    private static readonly Dictionary<string, List<(string Role, string Content)>> _sessions = new();
    private static readonly Dictionary<string, UserProfile> _profiles = new();

    public ChatController(GroqService groq, VectorStore vectors)
    {
        _groq = groq;
        _vectors = vectors;
    }

    [HttpPost("stream")]
    public async Task Stream([FromBody] ChatRequest req)
    {
        var sessionId = req.SessionId ?? Guid.NewGuid().ToString();
        if (!_sessions.ContainsKey(sessionId)) _sessions[sessionId] = new();
        if (!_profiles.ContainsKey(sessionId)) _profiles[sessionId] = new();

        var history = _sessions[sessionId];
        var profile = _profiles[sessionId];
        profile.MensajesCount++;

        // Busqueda semantica por similitud de cosenos
        var match = _vectors.FindBestMatch(req.Message, out double confidence);
        var intentHint = match != null ? $"{match.Intent} (confianza: {confidence})" : null;

        Response.ContentType = "text/event-stream";
        Response.Headers["Cache-Control"] = "no-cache";
        Response.Headers["Access-Control-Allow-Origin"] = "*";

        var meta = JsonSerializer.Serialize(new
        {
            type = "meta",
            session_id = sessionId,
            intent = match?.Intent ?? "general",
            quick_replies = new List<string>()
        });
        await Response.WriteAsync($"data: {meta}\n\n");
        await Response.Body.FlushAsync();

        var fullResponse = new StringBuilder();

        await foreach (var token in _groq.StreamAsync(req.Message, history, intentHint))
        {
            fullResponse.Append(token);
            if (!token.Contains("OPCIONES:"))
            {
                var payload = JsonSerializer.Serialize(new { type = "token", value = token });
                await Response.WriteAsync($"data: {payload}\n\n");
                await Response.Body.FlushAsync();
            }
        }

        var (cleanText, quickReplies) = ParseFull(fullResponse.ToString());

        history.Add(("user", req.Message));
        history.Add(("assistant", cleanText));
        if (history.Count > 20) _sessions[sessionId] = history.TakeLast(20).ToList();

        var done = JsonSerializer.Serialize(new { type = "done", quick_replies = quickReplies });
        await Response.WriteAsync($"data: {done}\n\n");
        await Response.Body.FlushAsync();
    }

    [HttpPost("reset/{sessionId}")]
    public IActionResult Reset(string sessionId)
    {
        _sessions.Remove(sessionId);
        _profiles.Remove(sessionId);
        return Ok(new { status = "ok" });
    }

    [HttpGet("/health")]
    public IActionResult Health() => Ok(new { status = "ok", service = "CENFE FitBot C#" });

    private static (string Text, List<string> QuickReplies) ParseFull(string full)
    {
        var lines = full.Split('\n').ToList();
        var qr = new List<string>();
        var text = new List<string>();
        foreach (var line in lines)
        {
            if (line.TrimStart().StartsWith("OPCIONES:"))
                qr = line.Replace("OPCIONES:", "").Trim()
                    .Split('|').Select(q => q.Trim())
                    .Where(q => !string.IsNullOrEmpty(q)).Take(3).ToList();
            else text.Add(line);
        }
        return (string.Join('\n', text).Trim(), qr);
    }
}
