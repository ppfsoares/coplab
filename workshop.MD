# Workshop de RAG com Gemini e Faiss

## Troubleshooting

- Erro ao ler arquivo .env no teste da API KEY

```bash
export $(grep -v '^#' /home/paula/coplab/.env | xargs)
python - << 'PY'
from google import genai
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
r = client.models.generate_content(model="gemini-2.5-flash", contents="Diga 'ok Gemini' em pt-br.")
print(r.text)
PY
```
