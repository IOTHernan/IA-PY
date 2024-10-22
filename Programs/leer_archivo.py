import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def main():
    file_path = input("Introduce la ruta del archivo de texto que deseas leer: ")
    text_to_read = read_file(file_path)
    if text_to_read:
        speak_text(text_to_read)

if __name__ == "__main__":
    main()
