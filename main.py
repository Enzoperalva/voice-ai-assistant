import services.ai_response as ar
import services.audio_transcription as at 
from google.genai.errors import ServerError
from time import sleep

if __name__ == "__main__": 
    with open("data/prompt.txt", "r", encoding='utf-8') as arq:
        prompt = arq.read()

    try:
        prompt_user = at.transcribe_with_gemini(
            audio_path="data/audio_for_ai.wav",
            prompt=prompt
        )
        prompt_user = prompt_user.strip()
        if prompt_user.lower() == 'none':
            print("Áudio do usuário está corrompido, silencioso ou inaudível.")

        else:
            print(f"PROMPT USER: {prompt_user}")
            response = ar.generate_response(prompt_user)
            
            print(f'PERGUNTA DO USUARIO:\n{prompt_user}')
            sleep(5)
            print()

            print('RESPOSTA IA: ')
            print(response)
    
    except ServerError:
        print('Gemini indisponível no momento. Tente novamente em alguns minutos')