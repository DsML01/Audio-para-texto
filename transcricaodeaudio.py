import whisper
import warnings

#ignora os avisos, pois são apenas avisos e não erros
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


#Carrega o modelo do whisper
model = whisper.load_model("small")

#Transcreve o áudio
result = model.transcribe("KARATE_KID.mp3")

with open("karate_kid.txt", "w", encoding = "utf-8") as arquivo:
    #Imprimir o texto transcrito
    for seg in result["segments"]:
        arquivo.write(f"[{seg['start']:.2f} - {seg['end']:.2f}] --> {seg['text']}\n")