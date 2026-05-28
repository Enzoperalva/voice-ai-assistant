import pyaudio, wave

audio = pyaudio.PyAudio()

stream = audio.open(
    input=True, 
    format=pyaudio.paInt16,  
    channels=1, 
    rate=44000, 
    frames_per_buffer=1024,    
)
frames = []

try:
    while True:
        bloco = stream.read(1024)
        frames.append(bloco)

except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

with wave.open("data/audio_for_ai.wav", "wb") as arq:
    arq.setnchannels(1)
    arq.setframerate(44000)
    arq.setsampwidth(audio.get_sample_size(pyaudio.paInt32))
    arq.writeframes(b"".join(frames))