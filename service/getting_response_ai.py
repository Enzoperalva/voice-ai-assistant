import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_KEY')

client = genai.Client(
    api_key=TOKEN
)

def response_ai(contents: str, model: str = "gemini-3.5-flash") -> str:
    response = client.models.generate_content(
        model=model,
        contents=contents
    )

    return response.text