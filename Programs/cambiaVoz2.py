import pyttsx3

engine = pyttsx3.init()

# Cambiar la voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Cambia el índice según la voz deseada

# Cambiar la velocidad
engine.setProperty('rate', 150)  # Ajusta la velocidad

# Hablar
engine.say("Hola, esta es la voz seleccionada.")
engine.runAndWait()
