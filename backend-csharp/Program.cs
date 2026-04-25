using CenfeFitBot;
using dotenv.net;

// Cargar .env si existe
DotEnv.Load(options: new DotEnvOptions(envFilePaths: new[] { "../.env", ".env" }));

var builder = WebApplication.CreateBuilder(args);

var groqApiKey = Environment.GetEnvironmentVariable("GROQ_API_KEY") ?? "";
var groqModel  = Environment.GetEnvironmentVariable("GROQ_MODEL") ?? "llama-3.3-70b-versatile";

// Servicios
builder.Services.AddControllers();
builder.Services.AddCors(o => o.AddDefaultPolicy(p =>
    p.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader()));

// Vector store — singleton con knowledge base precargada
builder.Services.AddSingleton<VectorStore>(_ =>
{
    var store = new VectorStore();
    KnowledgeBase.Seed(store);
    Console.WriteLine($"Vector store listo con {50} casos de uso");
    return store;
});

// Groq service
builder.Services.AddHttpClient();
builder.Services.AddScoped<GroqService>(sp =>
{
    var http = sp.GetRequiredService<IHttpClientFactory>().CreateClient();
    return new GroqService(http, groqApiKey, groqModel);
});

var app = builder.Build();

app.UseCors();
app.MapControllers();

var port = Environment.GetEnvironmentVariable("PORT") ?? "8080";
app.Run($"http://0.0.0.0:{port}");
