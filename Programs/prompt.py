import os
from datetime import datetime

import pyttsx3
import platform

# Inicializar el motor de síntesis de voz
def speak_text(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def show_prompt():
	try:
		while True:
			# Mostrar el prompt tipo DOS
			directorio_actual = os.getcwd()
			prompt_text = f"{directorio_actual}> "
			print(prompt_text, end='')
			speak_text(prompt_text)

			user_input = input()
			if user_input.lower() == 'exit':
				speak_text("Gracias por utilizar mi aplicación. ¡Hasta luego!")
				print("Saliendo...")
				break
			elif user_input.lower() == 'date':
				current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				speak_text(f"La fecha actual es {current_date}")
				print(f"La fecha actual es: {current_date}")
			elif user_input.lower() == 'help':
				help_text = "Ayuda: Puedes usar los comandos 'exit' para salir, 'date' para ver la fecha actual."
				speak_text(help_text)
				print(help_text)
			else:
				speak_text("Comando no reconocido. Por favor intenta de nuevo.")
				print("Comando no reconocido. Por favor intenta de nuevo.")
	except Exception as e:
		speak_text("Ha ocurrido un error.")
		print(f"Error: {e}")

if __name__ == "__main__":
	speak_text("Hola, ¿cómo estás? Este es un prompt interactivo. Escribe 'help' para ver los comandos disponibles.")
	show_prompt()
