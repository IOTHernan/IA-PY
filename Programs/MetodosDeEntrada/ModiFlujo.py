import threading
import time

# Variables globales
user_input = ""
voice_input = ""
combined_input = ""

def get_user_input():
    global user_input
    user_input = input("Escribí algo: ")

def recognize_speech():
    global voice_input
    # Simulación de reconocimiento de voz
    time.sleep(2)  # Espera para simular un retraso en el reconocimiento
    voice_input = "entrada por voz"

def main():
    global combined_input
    # Inicia el hilo para el reconocimiento de voz
    voice_thread = threading.Thread(target=recognize_speech)
    voice_thread.start()

    # Captura la entrada del usuario
    get_user_input()

    # Espera que el hilo de reconocimiento de voz termine
    voice_thread.join()

    # Combina las entradas, priorizando la primera
    if user_input:
        combined_input = user_input
    elif voice_input:
        combined_input = voice_input

    # Aquí podés procesar combined_input
    print(f"Entrada combinada: {combined_input}")

if __name__ == "__main__":
    main()
