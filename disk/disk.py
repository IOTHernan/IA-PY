# ▓▒░▓DISCOS▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
import curses
import datetime
import os
import platform
import shutil

import win32api
from termcolor import colored


def che_cd(unidad=None, directorio='.'):
    """
    Uso de che_cd:
    che_cd(unidad=None, directorio='.')

    :param unidad: La letra de la unidad en Windows (por ejemplo, 'D'). Ignorada en Linux.
    :param directorio: El directorio al que cambiar. Utiliza '/' como separador en Linux.

    - Cambia el directorio actual a la unidad y directorio especificado.
    - Si la unidad no es válida en Windows, se muestra un error.
    - Si el directorio no existe, se muestra un error.
    - En Linux, solo se cambia el directorio.
    - Si el sistema operativo no es soportado, se muestra un error.

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


def type_archivo(nombre):
    """
    Función para visualizar un archivo en modo scroll en la terminal.
    """
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
    """
    Y vuelve la información del volumen.
    :param path:
    :return:
    """
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
    """
    Lista de directorio
    :param path:
    :param show_all:
    :param detailed:
    :return:
    """
    try:
        # Obtener información del volumen
        volume_label, serial_number = get_volume_info(path)

        # Mostrar información del directorio
        print(f'Directorio: {path}')
        print(colored(f"Directorio listado: {path}", 'green'))
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
    """
    Crea un directorio si no existe.
    """
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directorio '{directory_path}' creado correctamente.")
        except OSError as e:
            print(f"Error al crear el directorio: {e}")
    else:
        print(f"Error el directorio '{directory_path}' ya existe.")


def rename_directory(old_directory_path, new_directory_path):
    """
    Renombra un directorio.
    Hola, muchos parámetros.
    """
    if os.path.exists(old_directory_path) & os.path.exists(new_directory_path):
        try:
            os.rename(old_directory_path, new_directory_path)
            print(f"Directorio '{old_directory_path}' renombrado a '{new_directory_path}'.")
        except OSError as e:
            print(f"Error al renombrar el directorio: {e}")
    else:
        print(f"El directorio '{old_directory_path}' no existe.")


def delete_directory(directory_path):
    """
    Que eliminar directorio.
    :param directory_path:
    :return:
    """
    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)
            print(f"Directorio '{directory_path}' eliminado correctamente.")
        except OSError as e:
            print(f"Error al eliminar el directorio: {e}")
    else:
        print(f"El directorio '{directory_path}' no existe.")

