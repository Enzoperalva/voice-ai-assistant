import os, google
from google import genai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_KEY')

if not TOKEN:
    raise RuntimeError('API KEY inválida') 

client = genai.Client(
    api_key=TOKEN
)

def generate_response(contents: str, model: str = "gemini-3.5-flash") -> str:
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents
        )     
        return response.text
    
    except google.api_core.exceptions.ResourceExhausted:
        return 'Erro: Você atingiu o limite de requisições (Rate Limit) da API.'

    except google.api_core.exceptions.DeadlineExceeded:
        return 'Erro: Operação demorou mais do que o tempo limite configurado.'
    
    except google.api_core.exceptions.ServiceUnavailable:
        return 'Erro: Serviço Indisponível.'

    except google.api_core.exceptions.InvalidArgument:
        return 'Erro: Conteúdo vazio/inválido ou não suportado'

    except google.api_core.exceptions.PermissionDenied:
        return 'Erro: Você não tem permissão.'