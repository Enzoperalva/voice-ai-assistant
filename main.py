import services.ai_response as ar
import services.audio_transcription as at 



print('PERGUNTA DO USUARIO: ')
print(at.prompt_user)

print()

print('RESPOSTA IA: ')

if __name__ == "__main__": 
    response = ar.response_ai(at.prompt_user)
    print(response)