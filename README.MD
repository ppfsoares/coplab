# Workshop de RAG com Gemini e Faiss

Origem: https://github.com/samuelcardoso/genai-copilot-lab/blob/main/WORKSHOP.md

## Preparar ambiente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

#listar todos os comandos criados
python main.py -help
```

## Prática

### Ativar o venv (caso não esteja ativo ainda)

```bash
source .venv/bin/activate
```

### 🌟 Listar modelos disponíveis

```bash
python main.py models
```

### Ingestão de regras

```bash
python main.py ingest-best --file ./dados/boas_praticas.txt
```

### Ingestão de código

```bash
python main.py ingest-code --dir ./testeRAG --ext ".py,.md,.txt"
```

### Chat

```bash
python main.py chat
```

### Pergunta única

```bash
python main.py ask --question "como melhorar a função X?"
```

### Reset

```bash
python main.py reset
```

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

## Aprendizados

A ingestão só faz sentido quando você **faz perguntas**. Execute:

```bash
python main.py chat
```

### Perguntas que usam a ingestão de CÓDIGO:

| Pergunta                                             | O que o sistema faz                                                                                            |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `Onde há senhas hardcoded?`                          | Busca no índice de código → encontra `src/calculadora.py` → cita o arquivo                                     |
| `Qual função não tem docstring?`                     | Busca no índice → encontra `def soma(a, b)` → aponta o problema                                                |
| `Tem funções muito longas?`                          | Busca no índice → analisa `processa_dados` → sugere refatoração                                                |
| `Nosso logging está de acordo com as boas práticas?` | busca nas boas práticas a regra de logging e no código a função processa_dados, notando a ausência de logging. |

### Perguntas que usam a ingestão de BOAS PRÁTICAS:

| Pergunta                             | O que o sistema faz                                |
| ------------------------------------ | -------------------------------------------------- |
| `Qual a cobertura de testes mínima?` | Busca no índice de boas práticas → responde "80%"  |
| `Como devo fazer logging?`           | Busca no índice → cita níveis INFO, WARNING, ERROR |

### Perguntas que usam AMBOS:

| Pergunta                                        | O que o sistema faz                                                                                 |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `O código segue as boas práticas de segurança?` | Cruza boas práticas (não hardcodar senhas) + código (encontra `senha = "123456"`) → aponta violação |

---

### Comprovando a Diferença

#### Teste 1: SEM ingestão de código

```bash
# Delete os arquivos de código
rm code_faiss.index code_chunks.pkl

# Inicie o chat
python main.py chat

# Pergunte:
>> Onde há senhas hardcoded?
```

**Resposta esperada:** "Não encontrei informações sobre isso no contexto." ❌

#### Teste 2: COM ingestão de código

```bash
# Re-ingira o código
python main.py ingest-code --dir ./testeRAG

# Inicie o chat
python main.py chat

# Pergunte:
>> Onde há senhas hardcoded?
```

**Resposta esperada:** "Encontrei em [FILE]: testeRAG/calc.py a linha `senha = "123456"`..." ✅

---
