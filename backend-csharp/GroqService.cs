using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace CenfeFitBot;

public class GroqService
{
    private readonly HttpClient _http;
    private readonly string _model;
    private const string API_URL = "https://api.groq.com/openai/v1/chat/completions";

    private const string SYSTEM_PROMPT = @"Eres FitBot, el asistente virtual del Gym CENFE.
Tu personalidad es: MUY motivador, energico, entusiasta y apasionado por el fitness.
Siempre respondes en el idioma del usuario (español o inglés).
Tu objetivo es ayudar, motivar e inspirar a los usuarios y convertir consultas en inscripciones.

Información del gym:
- Nombre: Gym CENFE | Slogan: Tu mejor version empieza aqui
- Planes: Basico $299/mes, Welcome $399/mes, Premium $599/mes, Elite $899/mes
- Horarios: Lun-Vie 5am-11pm | Sab 6am-9pm | Dom 7am-6pm
- Sucursales: Norte, Sur, Centro | Clase de prueba: GRATIS

Reglas:
1. Usa 3-5 emojis por respuesta para dar energia
2. Responde SIEMPRE en relacion directa a lo que preguntaron
3. Usa el historial para mantener contexto
4. Maximo 120 palabras por respuesta
5. Termina siempre con una pregunta o call to action
6. Usa **negritas** para destacar informacion importante
7. Al final de tu respuesta agrega: OPCIONES: opcion1 | opcion2 | opcion3";

    public GroqService(HttpClient http, string apiKey, string model)
    {
        _http = http;
        _model = model;
        _http.DefaultRequestHeaders.Authorization =
            new AuthenticationHeaderValue("Bearer", apiKey);
    }

    public async Task<(string Text, List<string> QuickReplies)> ChatAsync(
        string userMessage,
        List<(string Role, string Content)> history,
        string? intentHint = null)
    {
        var systemContent = SYSTEM_PROMPT;
        if (intentHint != null)
            systemContent += $"\n\nTema detectado: {intentHint}";

        var messages = new List<object>
        {
            new { role = "system", content = systemContent }
        };

        foreach (var (role, content) in history.TakeLast(8))
            messages.Add(new { role, content });

        messages.Add(new { role = "user", content = userMessage });

        var body = JsonSerializer.Serialize(new
        {
            model = _model,
            messages,
            max_tokens = 400,
            temperature = 0.7,
            stream = false
        });

        var response = await _http.PostAsync(API_URL,
            new StringContent(body, Encoding.UTF8, "application/json"));

        var json = await response.Content.ReadAsStringAsync();
        using var doc = JsonDocument.Parse(json);
        var fullText = doc.RootElement
            .GetProperty("choices")[0]
            .GetProperty("message")
            .GetProperty("content")
            .GetString() ?? "";

        return ParseResponse(fullText);
    }

    public async IAsyncEnumerable<string> StreamAsync(
        string userMessage,
        List<(string Role, string Content)> history,
        string? intentHint = null)
    {
        var systemContent = SYSTEM_PROMPT;
        if (intentHint != null)
            systemContent += $"\n\nTema detectado: {intentHint}";

        var messages = new List<object>
        {
            new { role = "system", content = systemContent }
        };
        foreach (var (role, content) in history.TakeLast(8))
            messages.Add(new { role, content });
        messages.Add(new { role = "user", content = userMessage });

        var body = JsonSerializer.Serialize(new
        {
            model = _model,
            messages,
            max_tokens = 400,
            temperature = 0.7,
            stream = true
        });

        var request = new HttpRequestMessage(HttpMethod.Post, API_URL)
        {
            Content = new StringContent(body, Encoding.UTF8, "application/json")
        };

        using var response = await _http.SendAsync(request,
            HttpCompletionOption.ResponseHeadersRead);
        using var stream = await response.Content.ReadAsStreamAsync();
        using var reader = new StreamReader(stream);

        while (!reader.EndOfStream)
        {
            var line = await reader.ReadLineAsync();
            if (string.IsNullOrEmpty(line) || !line.StartsWith("data: ")) continue;
            var data = line[6..];
            if (data == "[DONE]") break;

            using var doc = JsonDocument.Parse(data);
            var delta = doc.RootElement
                .GetProperty("choices")[0]
                .GetProperty("delta");

            if (delta.TryGetProperty("content", out var content))
            {
                var token = content.GetString();
                if (!string.IsNullOrEmpty(token))
                    yield return token;
            }
        }
    }

    private static (string Text, List<string> QuickReplies) ParseResponse(string full)
    {
        var lines = full.Split('\n').ToList();
        var quickReplies = new List<string>();
        var textLines = new List<string>();

        foreach (var line in lines)
        {
            if (line.TrimStart().StartsWith("OPCIONES:"))
            {
                var raw = line.Replace("OPCIONES:", "").Trim();
                quickReplies = raw.Split('|')
                    .Select(q => q.Trim())
                    .Where(q => !string.IsNullOrEmpty(q))
                    .Take(3).ToList();
            }
            else textLines.Add(line);
        }

        return (string.Join('\n', textLines).Trim(), quickReplies);
    }
}
