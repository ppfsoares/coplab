import os
from typing import List, Tuple
from google import genai

def list_available_models(client: genai.Client) -> Tuple[List[str], List[str]]:
    """Lista todos os modelos disponíveis para sua chave API com debug detalhado."""
    print("\n" + "="*70)
    print("🔍 DIAGNÓSTICO DE CONEXÃO COM GEMINI API")
    print("="*70)
    
    # LOG 1: Verificar cliente
    print("\n[1/5] Verificando cliente Gemini...")
    print(f"  • Tipo do cliente: {type(client)}")
    print(f"  • Cliente criado: {client is not None}")
    
    # LOG 2: Verificar API Key
    print("\n[2/5] Verificando API Key...")
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print(f"  • API Key encontrada: SIM")
        print(f"  • Tamanho da chave: {len(api_key)} caracteres")
        print(f"  • Primeiros 8 chars: {api_key[:8]}...")
        print(f"  • Últimos 4 chars: ...{api_key[-4:]}")
    else:
        print(f"  • API Key encontrada: NÃO ❌")
        print("  → ERRO: GEMINI_API_KEY não está definida no .env")
        return [], []
    
    # LOG 3: Tentar listar modelos
    print("\n[3/5] Tentando listar modelos da API...")
    try:
        print("  • Chamando client.models.list()...")
        models = client.models.list()
        print(f"  • Resposta recebida: {type(models)}")
        
        model_list = []
        try:
            for i, m in enumerate(models):
                model_list.append(m)
                if i < 3:
                    print(f"    [{i}] Modelo: {m}")
                    print(f"        • Tipo: {type(m)}")
                    print(f"        • Atributos: {[attr for attr in dir(m) if not attr.startswith('_')][:10]}")
        except Exception as iter_err:
            print(f"  • Erro ao iterar modelos: {iter_err}")
        
        print(f"  • Total de modelos brutos: {len(model_list)}")
        
    except Exception as e:
        print(f"  • ERRO na chamada API: {type(e).__name__}")
        print(f"  • Mensagem: {e}")
        print(f"  • Args do erro: {getattr(e, 'args', 'N/A')}")
        print("\n  💡 Possíveis soluções:")
        print("     1. Verifique se a API Key está correta no .env")
        print("     2. Teste sua chave em: https://aistudio.google.com/app/apikey")
        print("     3. Atualize o SDK: pip install --upgrade google-genai")
        print("     4. Verifique sua conexão com a internet")
        return [], []
    
    # LOG 4: Processar modelos
    print("\n[4/5] Processando modelos...")
    chat_models = []
    embed_models = []
    
    for i, m in enumerate(model_list):
        try:
            name = getattr(m, 'name', 'SEM_NOME')
            methods = getattr(m, 'supported_generation_methods', [])
            
            if i < 5:
                print(f"  • Modelo {i}: {name}")
                print(f"    - Métodos: {methods}")
            
            if methods:
                if 'generateContent' in methods:
                    chat_models.append(name)
                if 'embedContent' in methods or 'embed' in str(methods).lower():
                    embed_models.append(name)
            else:
                if 'embedding' in name.lower():
                    embed_models.append(name)
                elif 'flash' in name.lower() or 'pro' in name.lower():
                    chat_models.append(name)
                    
        except Exception as model_err:
            print(f"  • Erro ao processar modelo {i}: {model_err}")
            continue
    
    # LOG 5: Resultados finais
    print("\n[5/5] Resultados:")
    print("-"*70)
    print(f"🗣️  MODELOS DE CHAT ({len(chat_models)} encontrados):")
    for model in sorted(chat_models):
        print(f"  ✅ {model}")
    
    print(f"\n📊 MODELOS DE EMBEDDING ({len(embed_models)} encontrados):")
    for model in sorted(embed_models):
        print(f"  ✅ {model}")
    
    print("-"*70)
    
    if len(chat_models) == 0 and len(embed_models) == 0:
        print("\n⚠️  NENHUM MODELO ENCONTRADO!")
        print("\n💡 Ações recomendadas:")
        print("   1. Verifique se sua chave API tem permissões ativas")
        print("   2. Acesse https://aistudio.google.com/ e teste a chave manualmente")
        print("   3. Tente criar uma NOVA chave API")
        print("   4. Verifique se há restrições de região na sua conta")
        print("   5. Execute: pip install --upgrade google-genai")
    else:
        print(f"\n💡 Use um dos modelos acima no seu arquivo .env")
        if chat_models:
            print(f"   Exemplo: GEMINI_CHAT_MODEL=\"{chat_models[0]}\"")
        if embed_models:
            print(f"   Exemplo: GEMINI_EMBED_MODEL=\"{embed_models[0]}\"")
    
    print("="*70 + "\n")
    
    return chat_models, embed_models