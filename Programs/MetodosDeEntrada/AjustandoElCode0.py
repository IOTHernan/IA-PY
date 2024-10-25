import threading
import time

def recognize_speech():
    global voice_input
    while True:
        # Aquí iría el código que reconoce el habla
        voice_input = "Reconocido desde voz"  # Simulación de entrada de voz
        time.sleep(5)  # Simula el tiempo de espera entre reconocimientos

def get_user_input():
    while True:
        user_input = input("Ingresa tu texto: ")
        if user_input.lower() == "salir":
            break
        print(f"Texto ingresado: {user_input}")

def main():
    global voice_input
    voice_input = ""  # Inicializamos la variable global para la entrada de voz

    # Crear y empezar el thread para el reconocimiento de voz
    speech_thread = threading.Thread(target=recognize_speech)
    speech_thread.daemon = True  # Permitir que el hilo se cierre cuando el programa principal termine
    speech_thread.start()

    # Bucle principal
    while True:
        # Aquí actualizamos las variables de entrada
        user_input = get_user_input()
        print(f"Entrada de voz actual: {voice_input}")

        # Aquí podrías manejar las entradas según tu lógica
        if user_input.lower() == "salir":
            break

    # Esperar a que termine el hilo de reconocimiento (opcional)
    speech_thread.join()

if __name__ == "__main__":
    main()
