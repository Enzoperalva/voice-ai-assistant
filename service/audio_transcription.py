import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
TOKEN = os.getenv('API_KEY')

client = genai.Client(
    api_key=TOKEN
)

def transcibe_with_gemini(audio_path: str, model: str = "gemini-3.5-flash", prompt: str | None = None) -> str:
    audio_file = client.files.upload(file=audio_path)
    
    response = client.models.generate_content(
        model= model,
        contents= [
            prompt,
            audio_file
        ]
    )

    return response.text


with open("data/prompt.txt", "r", encoding='utf-8') as arq:
    prompt = arq.read()

prompt_user = transcibe_with_gemini(
    audio_path="data/audio_for_ai.wav",
    prompt=prompt
)