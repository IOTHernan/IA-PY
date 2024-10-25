import threading
import time

class InputHandler:
    def __init__(self):
        self.user_input = None
        self.voice_input = None
        self.combined_input = None
        self.voice_thread = None

    def get_user_input(self):
        self.user_input = input("Escribí algo: ")

    def recognize_speech(self):
        # Simulación de reconocimiento de voz
        time.sleep(2)  # Simula un retraso
        self.voice_input = "entrada por voz"

    def process_inputs(self):
        # Se decide cuál entrada usar
        if self.user_input is not None:
            self.combined_input = self.user_input
        elif self.voice_input is not None:
            self.combined_input = self.voice_input

    def run(self):
        # Inicia el hilo para el reconocimiento de voz
        self.voice_thread = threading.Thread(target=self.recognize_speech)
        self.voice_thread.start()

        # Captura la entrada del usuario
        self.get_user_input()

        # Espera que el hilo de reconocimiento de voz termine
        self.voice_thread.join()

        # Procesa las entradas
        self.process_inputs()

        # Mostrar la entrada combinada
        print(f"Entrada combinada: {self.combined_input}")


if __name__ == "__main__":
    input_handler = InputHandler()
    input_handler.run()
