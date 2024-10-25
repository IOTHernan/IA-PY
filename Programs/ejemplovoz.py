from vosk import Model, KaldiRecognizer
import googletrans
import json
import pyaudio

# Configurar el modelo de Vosk
model = Model("C:/ChipSoft/Python/vosk/vosk-model-es-0.42/vosk-model-es-0.42")
recognizer = KaldiRecognizer(model, 16000)

# Configurar Googletrans
translator = googletrans.Translator()

# Capturar audio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Di algo...")

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        texto = result['text']
        if texto:
            print(f"Texto reconocido: {texto}")
            traduccion = translator.translate(texto, src='en', dest='es')
            print(f"Traducción: {traduccion.text}")
