# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform

if platform.system() == 'Windows':
    try:
        import windows_curses as curses
        import win32api
    except ImportError:
        print("Instala 'windows-curses' con pip para usar curses en Windows.")
else:
    import curses

# Tu código que usa curses va aquí

# import argparse
import PyPDF2
import os
import pathlib
import shutil
import pyperclip
import pickle
import pyttsx3
import time
import speech_recognition as sr
import pyaudio
import psutil
from google.cloud import translate_v2 as translate
from datetime import datetime
from termcolor import colored
import httpx
from googletrans import Translator


def speak_text(text):
    """Función para sintetizar y reproducir voz a partir de texto."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


#@memory_monitor
def translate_text(text, src='en', dest='es'):
    translator = Translator()
    return translator.translate(text, src=src, dest=dest).text


def translate_text_gcp(text, target='es'):
    """Función para traducir texto usando Google Cloud Translate."""
    client = translate.Client()
    result = client.translate(text, target_language=target)
    return result['translatedText']


def help_translate_text():
    """Función para traducir texto usando Google Cloud Translate.
    Sintaxis: traducir palabra lenguaje"""
    print("""Comando: traducir palabra lenguaje lenguaje""")


def save_dict(data_dict, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data_dict, file)


def load_dict(file_path):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error cargando el diccionario: {e}")
        return {}


# def read_file(file_path):
#     """Lee el contenido de un archivo."""
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         print(f"Error: El archivo '{file_path}' no se encontró.")
#     except PermissionError:
#         print(f"Error: No tienes permisos para leer el archivo '{file_path}'.")
#     except IOError as e:
#         print(f"Error de E/S: {e}")
#     return None
def copy_to_clipboard(content):
    """Copia el contenido proporcionado al portapapeles."""
    pyperclip.copy(content)
    print("El contenido ha sido copiado al portapapeles.")


def check_disk_space(path, min_free_space):
    """Verifica si hay al menos min_free_space bytes libres en el disco."""
    total, used, free = shutil.disk_usage(path)
    if free < min_free_space:
        raise IOError("No hay suficiente espacio en disco. Espacio libre: {} bytes".format(free))


def read_file(file_path):
    """Lee el contenido de un archivo y maneja posibles excepciones."""
    try:
        # Verificar espacio en disco antes de leer el archivo
        check_disk_space("/", 1024 * 1024 * 100)  # Por ejemplo, mínimo 100MB de espacio libre
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{file_path}'.")
    except IOError as e:
        print(f"Error de E/S: {e}")


def generate_java_code(content):
    """Genera el código Java Maven a partir del contenido leído."""
    # Implementar la lógica para generar el código aquí
    # Esto es solo un ejemplo de cómo podrías empezar
    java_code = "// Generado automáticamente\n"
    java_code += content
    return java_code


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(colored(f'Hi, {name}', 'blue'))  # Press Ctrl+F8 to toggle the breakpoint.


def read_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"Error leyendo el archivo binario: {e}")
        return None


def write_binary_file(file_path, data):
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
    except Exception as e:
        print(f"Error escribiendo el archivo binario: {e}")

# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░

def help(nombre):
    """
    Este es un ejemplo de módulo de ayuda.
    Puedes documentar tus funciones y módulos aquí.
    Exit: Sale de la aplicación.
    Help: Muestra esta ayuda.
    Type: Muestra contenido de archivo. Sintaxis: Type archivo.ext
    """
    print(colored(help.__doc__,'green'))
    print(colored("Crazy", 'red'))


def exist(nombre):
    file_path = pathlib.Path(nombre)
    if file_path.exists():
        return True
    else:
        return False




def che_if(nombre):
    if os.path.exists(nombre):
        speak_text('El archivo existe')
        return True
    else:
        speak_text('El archivo no existe')
        return False


def che_date():
    from datetime import datetime
    print(datetime.now())


# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░


def verifica_audio():
    try:
        pyaudio.PyAudio()
        print("PyAudio está instalado correctamente.")
    except Exception as e:
        print(f"Error con PyAudio: {e}")

    # Verifica si speech_recognition está funcionando
    try:
        recognizer = sr.Recognizer()
        print("speech_recognition está instalado correctamente.")
    except Exception as e:
        print(f"Error con speech_recognition: {e}")


def analyze_input(user_input):
    # Aquí puedes agregar la lógica para analizar la entrada y ejecutar la función correspondiente
    print(f"Analizando entrada: {user_input}")
    # Ejemplo: Solo para propósitos de demostración
    if user_input == "saludo":
        print("¡Hola! ¿Cómo estás?")
    else:
        print("Entrada no reconocida.")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando al ruido ambiente, por favor espere...")
        recognizer.adjust_for_ambient_noise(source)
        print("Di algo!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("No pude entender el audio.")
            return ""
        except sr.RequestError as e:
            print(f"No pude solicitar resultados del servicio de reconocimiento de voz; {e}")
            return ""


# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
def che_cd(unidad=None, directorio='.'):
    """
    Cambia el directorio actual a una unidad y/o directorio específico.

    :param unidad: La letra de la unidad en Windows (por ejemplo, 'D'). Ignorada en Linux.
    :param directorio: El directorio al que cambiar. Utiliza '/' como separador en Linux.
    :return: None
    :raises: OSError si el sistema operativo no es soportado, FileNotFoundError si el directorio no existe, OSError si la unidad no es válida.
    """
    sistema = platform.system()

    try:
        if sistema == 'Windows':
            if unidad:
                # Cambiar a la unidad especificada
                try:
                    os.chdir(f"{unidad}:\\")
                except FileNotFoundError:
                    raise OSError(f"Unidad '{unidad}:' no encontrada o no es válida.")
            # Cambiar al directorio especificado en la unidad actual
            try:
                os.chdir(directorio)
            except FileNotFoundError:
                raise FileNotFoundError(f"El directorio '{directorio}' no existe.")

        elif sistema == 'Linux':
            # En Linux solo cambia al directorio especificado
            try:
                os.chdir(directorio)
            except FileNotFoundError:
                raise FileNotFoundError(f"El directorio '{directorio}' no existe.")

        else:
            raise OSError("Sistema operativo no soportado.")

        # Mostrar el directorio actual
        print("Directorio actual:", os.getcwd())

    except OSError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def help_che_cd():
    """
    Muestra la ayuda para la función che_cd.
    """
    print("""
    Uso de che_cd:
    che_cd(unidad=None, directorio='.')

    :param unidad: La letra de la unidad en Windows (por ejemplo, 'D'). Ignorada en Linux.
    :param directorio: El directorio al que cambiar. Utiliza '/' como separador en Linux.

    - Cambia el directorio actual a la unidad y directorio especificado.
    - Si la unidad no es válida en Windows, se muestra un error.
    - Si el directorio no existe, se muestra un error.
    - En Linux, solo se cambia el directorio.
    - Si el sistema operativo no es soportado, se muestra un error.
    """)


def type_archivo(nombre):
    """Función para visualizar un archivo en modo scroll en la terminal."""
    if os.path.exists(nombre):
        def main(stdscr):
            # Inicializa la pantalla y desactiva el cursor
            curses.curs_set(0)
            # Carga el contenido del archivo
            with open(nombre, 'r') as file:
                lines = file.readlines()
            # Dimensiones de la ventana
            height, width = stdscr.getmaxyx()
            # Inicializa variables para controlar la posición del scroll
            current_line = 0
            max_lines = len(lines)
            while True:
                stdscr.clear()
                # Determina el rango de líneas a mostrar en la ventana actual
                for i, line in enumerate(lines[current_line:current_line + height - 1]):
                    stdscr.addstr(i, 0, line[:width - 1])

                # Refresca la pantalla para mostrar los cambios
                stdscr.refresh()

                # Captura la entrada del usuario
                key = stdscr.getch()

                # Desplazamiento hacia arriba
                if key == curses.KEY_UP and current_line > 0:
                    current_line -= 1

                # Desplazamiento hacia abajo
                elif key == curses.KEY_DOWN and current_line < max_lines - height + 1:
                    current_line += 1

                # Salir con la tecla 'q'
                elif key == ord('q'):
                    break

        # Ejecuta la aplicación de curses
        curses.wrapper(main)
    else:
        print(f"El archivo '{nombre}' no existe.")


# Función para listar archivos y directorios
def get_free_space(path):
    if platform.system() == 'Windows':
        # Para Windows, usa shutil.disk_usage
        total, used, free = shutil.disk_usage(path)
    else:
        # Para Unix/Linux/Mac, usa os.statvfs
        statvfs = os.statvfs(path)
        free = statvfs.f_frsize * statvfs.f_bavail
    return free


def get_volume_info(path):
    try:
        if platform.system() == 'Windows':
            drive = os.path.splitdrive(path)[0]
            if not drive:  # Si no se puede obtener la unidad, usa 'C:'
                drive = 'C:'
            volume_info = win32api.GetVolumeInformation(drive)
            volume_label = volume_info[0]
            serial_number = volume_info[1]
            return volume_label, serial_number
        else:
            return "N/A", "N/A"
    except Exception as e:
        print(f"Error obteniendo información del volumen: {e}")
        return "N/A", "N/A"


def list_directory(path='.', show_all=False, detailed=False):
    try:
        # Obtener información del volumen
        volume_label, serial_number = get_volume_info(path)

        # Mostrar información del directorio
        print(f'Directorio: {path}')
        print(colored(f"Directorio listado: {path}",'green'))
        print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Volumen: {volume_label} (Número de serie: {serial_number})")

        entries = os.listdir(path)

        if not show_all:
            entries = [entry for entry in entries if not entry.startswith('.')]

        total_size = 0
        file_count = 0
        dir_count = 0

        for entry in entries:
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                dir_count += 1
                entry_type = 'Directorio'
                size = 'N/A'
            else:
                file_count += 1
                entry_type = 'Archivo'
                stats = os.stat(entry_path)
                size = stats.st_size
                total_size += size

            if detailed:
                date_modified = datetime.fromtimestamp(stats.st_mtime).strftime(
                    '%Y-%m-%d %H:%M:%S') if not os.path.isdir(entry_path) else 'N/A'
                print(f"{entry: <30} {entry_type: <10} {size: >10} bytes {date_modified}")

        print(f"\nCantidad de archivos: {file_count}")
        print(f"Tamaño total de archivos: {total_size} bytes ({total_size / (1024 * 1024):.2f} MB)")
        print(f"Cantidad de directorios: {dir_count}")
        print(f"Espacio libre en disco: {get_free_space(path) / (1024 * 1024):.2f} MB")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el directorio {path}")


def create_directory(directory_path):
    """Crea un directorio si no existe."""
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directorio '{directory_path}' creado correctamente.")
        except OSError as e:
            print(f"Error al crear el directorio: {e}")
    else:
        print(f"Error el directorio '{directory_path}' ya existe.")



def rename_directory(old_directory_path, new_directory_path):
    """Renombra un directorio."""
    if os.path.exists(old_directory_path) & os.path.exists(new_directory_path):
        try:
            os.rename(old_directory_path, new_directory_path)
            print(f"Directorio '{old_directory_path}' renombrado a '{new_directory_path}'.")
        except OSError as e:
            print(f"Error al renombrar el directorio: {e}")
    else:
        print(f"El directorio '{old_directory_path}' no existe.")


def delete_directory(directory_path):
    """Elimina un directorio."""
    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)
            print(f"Directorio '{directory_path}' eliminado correctamente.")
        except OSError as e:
            print(f"Error al eliminar el directorio: {e}")
    else:
        print(f"El directorio '{directory_path}' no existe.")


# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
def main():
    print("Estás en main...")
    while True:
        # Mostrar el prompt tipo DOS
        directorio_actual = os.getcwd()
        user_input = input(colored(f"{directorio_actual}>",'red'))

        # Salir si el usuario escribe 'exit'
        if user_input.lower() == "exit":
            speak_text("Gracias por utilizar mi aplicación.  ")
            print("Saliendo...")
            break

        # Parsear el comando ingresado
        parts = user_input.split()
        print("len parts", len(parts))
        if len(parts) > 1:
            for x in range(len(parts)):
                print(f"{x} {parts[x]}")
        else:
            continue

        if parts[0].lower() == "traducir":
            if len(parts) > 1:
                translate_text(parts[1],parts[2],parts[3])
                continue
        if parts[0].lower() == "md" or parts[0].lower() == "mkdir":
            if len(parts) > 1:
                directory_path = parts[1]
                create_directory(directory_path)
                continue
        if parts[0].lower() == "rmdir" or parts[0].lower() == "rm":
            if len(parts) > 1:
                directory_path = parts[1]
                delete_directory(directory_path)
                continue
        if parts[0].lower() == "rename" or parts[0].lower() == "mv":
            if len(parts) > 2:
                old_directory_path = parts[1]
                new_directory_path = parts[2]
                speak_text('Renombrando {old_directory_path} a {new_directory_path}')
                rename_directory(old_directory_path, new_directory_path)
                continue
        if parts[0].lower() == "exists":
            if len(parts) > 1:
                directory_path = parts[1]
                che_if(directory_path)
                continue
        if parts[0].lower() == "help":
            speak_text("Ayuda")
            help()
            continue
        if parts[0].lower() == "date":
            speak_text("La fecha actual es:")
            che_date()
            continue
        if user_input.lower() == "audio":
            verifica_audio()
            continue
        if parts[0].lower() == 'type':
            speak_text('Visualizando archivo')
            if len(parts) > 1:
                archivo = parts[1]
                type_archivo(archivo)
        if parts[0].lower() == 'typepdf':
            speak_text('Visualizando archivo ')
            if len(parts) > 1:
                try:
                    with open(parts[1],"rb") as f:
                        reader = PyPDF2.PdfReader(f)
                        for page in reader.pages:
                            print(page.extract_text())
                except FileNotFoundError:
                    print("El archivo no fue encontrado.")
                except Exception as e:
                    print(f"Ocurrió un error al leer el PDF: {e}")
        if parts[0].lower() == 'dir':
            speak_text('Listando archivos')
            path = '.'
            show_all = False
            detailed = False

            if len(parts) > 1:
                for part in parts[1:]:
                    if part == '/a':
                        show_all = True
                    elif part == '/w':
                        detailed = False
                    elif part == '/l':
                        detailed = True
                    else:
                        path = part

            # Llamar a la función con los parámetros obtenidos
            list_directory(path=path, show_all=show_all, detailed=detailed)
        else:
            print("Comando no reconocido. Por favor, ingresa 'dir [path] [opciones]' o 'exit' para salir.")
        # continue

        # Analizar entrada por teclado
        analyze_input(user_input)

        # También puedes escuchar entrada por voz
        print(colored("Ahora escuchando...","yellow"))
        voice_input = recognize_speech()
        print(f"Entrada de voz: {voice_input}")
        if voice_input:
            print(f"Entrada de voz: {voice_input}")
            if voice_input.lower() == "exit":
                print("Saliendo...")
                break
            analyze_input(voice_input)

        # Mostrar prompt nuevamente
        print("Ingrese otro comando o diga algo (escriba 'exit' para salir):")


if __name__ == "__main__":
    print("Hola! Soy AtomSophy! ¿Cómo estás?")
    speak_text("Hola soy AtomSophy, ¿cómo estás?, usando PiCharm")
    # Ejemplo de uso
    # translated = translate_text('Hello, world!', 'es')
    # print(translated)  # Salida esperada: '¡Hola, mundo!'
    # t = translate_text("Common")
    # print("Translate: ")
    # print(t)
    # help()
    main()
    # file_path = "ruta/al/archivo.txt"
    # content = read_file(file_path)
    # if content:
    #     java_code = generate_java_code(content)
    #     print(java_code)

    # Press the green button in the gutter to run the script.
    # if __name__ == '__main__':
    # Ejemplo de uso

    # Ejemplo de uso
    # recognize_speech()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # if __name__ == "__main__":
    #     file_path = "ruta/al/archivo.txt"
    #     content = read_file(file_path)
    #     if content:
    #   copy_to_clipboard(content)
