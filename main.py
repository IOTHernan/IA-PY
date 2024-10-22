# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import os
import shutil

import pyperclip

import pickle

from googletrans import Translator

def translate_text(text, src='en', dest='es'):
    translator = Translator()
    return translator.translate(text, src=src, dest=dest).text

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
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
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

def help():
    """
    Este es un ejemplo de módulo de ayuda.
    Puedes documentar tus funciones y módulos aquí.
    """
    print(help.__doc__)
    print("Crazy")


if __name__ == "__main__":
    # file_path = "ruta/al/archivo.txt"
    # content = read_file(file_path)
    # if content:
    #     java_code = generate_java_code(content)
    #     print(java_code)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    print_hi('PyCharm')
    t = translate_text("Common")
    print("Translate: ")
    print(t)
    help()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# if __name__ == "__main__":
#     file_path = "ruta/al/archivo.txt"
#     content = read_file(file_path)
#     if content:
#         copy_to_clipboard(content)