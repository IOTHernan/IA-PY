import threading
import time


def recognize_speech():
	global voice_input
	while True:
		# Simulación de entrada de voz
		voice_input = "Entrada de voz reconocida"  # Simulación de entrada de voz
		time.sleep(5)  # Simula el tiempo de espera entre reconocimientos


def get_user_input():
	while True:
		user_input = input("Ingresa tu texto: ")
		if user_input.lower() == "salir":
			return None  # Devolvemos None para salir del bucle principal
		return user_input  # Retornamos la entrada del usuario


def main():
	global voice_input
	voice_input = ""  # Inicializamos la variable global para la entrada de voz

	# Crear y empezar el thread para el reconocimiento de voz
	speech_thread = threading.Thread(target=recognize_speech)
	speech_thread.daemon = True  # Permitir que el hilo se cierre cuando el programa principal termine
	speech_thread.start()

	# Bucle principal
	while True:
		user_input = get_user_input()
		print(f"Entrada de voz actual: {voice_input}")

		if user_input is None:  # Verificamos si el usuario quiere salir
			break

		# Aquí combinamos ambas entradas
		combined_input = f"{user_input} {voice_input}"
		parts = combined_input.lower().split()
		print(f"Partes de la entrada combinada: {parts}")

		# Manejo de las partes
		if parts:  # Solo si hay partes
			primera_parte = parts[0]
			print(f"Primera parte: {primera_parte}")

	# Esperar a que termine el hilo de reconocimiento (opcional)
	speech_thread.join()


if __name__ == "__main__":
	main()
