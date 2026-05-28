import services.ai_response as ar
import services.audio_transcription as at 

if __name__ == "__main__": 
    with open("data/prompt.txt", "r", encoding='utf-8') as arq:
        prompt = arq.read()

    prompt_user = at.transcribe_with_gemini(
        audio_path="data/audio_for_ai.wav",
        prompt=prompt
    )

    print(f'PERGUNTA DO USUARIO:\n{prompt_user}')

    print()

    print('RESPOSTA IA: ')
    response = ar.generate_response(prompt_user)
    print(response)