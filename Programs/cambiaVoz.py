import pyttsx3

engine = pyttsx3.init()

# Listar voces disponibles
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Cambiar a una voz específica (por ejemplo, la voz 0)
engine.setProperty('voice', voices[0].id)  # Cambia 0 por el índice deseado

# Para hablar
engine.say("Hola, esta es la voz seleccionada.")
engine.runAndWait()
