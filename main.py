import service.getting_response_ai as gr
import service.audio_transcription as at 



print('PERGUNTA DO USUARIO: ')
print(at.prompt_user)

print()

print('RESPOSTA IA: ')

if __name__ == "__main__": 
    response = gr.response_ai(at.prompt_user)
    print(response)