import platform
import googletrans
from vosk import Model, KaldiRecognizer
import os
import pyperclip
import pickle
import speech_recognition as sr
import pyaudio
from termcolor import colored
import threading
import PyPDF2
import json
from datetime import datetime
from disk import (create_directory, delete_directory, rename_directory, type_archivo,
                  list_directory, check_disk_space, get_free_space, get_volume_info, che_if, che_cd)
from che_text import speak_text, translate_text, read_file_to_speaker

if platform.system() == 'Windows':
	try:
		import windows_curses as curses
		import win32api
	except ImportError:
		print("Instala 'windows-curses' con pip para usar curses en Windows.")
else:
	import curses

# Cargar modelo Vosk
#model = Model("C:\ChipSoft\Python\vosk\vosk-model-es-0.42\vosk-model-es-0.42")
model = Model("C:/ChipSoft/Python/vosk/vosk-model-es-0.42/vosk-model-es-0.42")
recognizer = KaldiRecognizer(model, 16000)

# Configurar Googletrans
translator = googletrans.Translator()
global voice_input

# Guardar y cargar diccionario
def save_dict(data_dict, file_path):
	"""
	Salvado bendiciones.
	:param data_dict:
	:param file_path:
	:return:
	"""
	with open(file_path, 'wb') as file:
		pickle.dump(data_dict, file)

def load_dict(file_path):
	"""
	Lectura del diccionario.
	:param file_path:
	:return:
	"""
	try:
		with open(file_path, 'rb') as file:
			return pickle.load(file)
	except Exception as e:
		print(f"Error cargando el diccionario: {e}")
		return {}

def copy_to_clipboard(content):
	"""
	Copia el contenido proporcionado al portapapeles.
	"""
	pyperclip.copy(content)
	print("El contenido ha sido copiado al portapapeles.")

def read_file(file_path):
	"""
	Lee el contenido de un archivo y maneja posibles excepciones.
	"""
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
	"""
	Genera el código Java Maven a partir del contenido leído.
	"""
	# Implementar la lógica para generar el código aquí
	# Esto es solo un ejemplo de cómo podrías empezar
	java_code = "// Generado automáticamente\n"
	java_code += content
	return java_code

def print_hi(name):
	"""
	Increíble con la lumbeis.
	:param name:
	:return:
	"""
	# Use a breakpoint in the code line below to debug your script.
	print(colored(f'Hi, {name}', 'blue'))  # Press Ctrl+F8 to toggle the breakpoint.

def read_binary_file(file_path):
	"""
	Lee un archivo vídeo
	:param file_path:
	:return:
	"""
	try:
		with open(file_path, 'rb') as file:
			return file.read()
	except Exception as e:
		print(f"Error leyendo el archivo binario: {e}")
		return None

def write_binary_file(file_path, data):
	"""
	Escribe un archivo binario
	:param file_path:
	:param data:
	:return:
	"""
	try:
		with open(file_path, 'wb') as file:
			file.write(data)
	except Exception as e:
		print(f"Error escribiendo el archivo binario: {e}")

# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
def che_date():
	"""
	Imprime la fecha.
	:return:
	"""
	from datetime import datetime
	print(datetime.now())

# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
def get_user_input():
	"""
	Esta función es retorna la entrada por teclado.
	:return:
	"""
	user_input_text: str = input()
	return user_input_text

def verifica_audio():
	"""
	Esta función verifica el audio entrada.
	:return:
	"""
	try:
		pyaudio.PyAudio()
		print("PyAudio está instalado correctamente.")
	except Exception as e:
		print(f"Error con PyAudio: {e}")

	# Verifica si speech_recognition está funcionando
	try:
		# recognizer = sr.Recognizer()
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
		print("Recognize_speech Ajustando al ruido ambiente, por favor espere...")
		recognizer.adjust_for_ambient_noise(source)
		print("Recognize_speech Te escucho!")
		audio = recognizer.listen(source)
		try:
			text = recognizer.recognize_google(audio)
			return text
		except sr.UnknownValueError:
			print("Recognize_speech No puede entender el audio.")
			return ""
		except sr.RequestError as e:
			print(f"No pude solicitar resultados del servicio de reconocimiento de voz; {e}")
			return ""

def entrada_voz():
	# También puedes escuchar entrada por voz
	print(colored("entrada_voz Ahora escuchando...", "yellow"))
	voice_input = recognize_speech()
	print(f"Entrada de voz: {voice_input}")
	if voice_input:
		print(f"Entrada de voz: {voice_input}")
		if voice_input.lower() == "exit":
			print("Saliendo...")

		analyze_input(voice_input)

	# Mostrar prompt nuevamente
	print("Ingrese otro comando o diga algo (escriba 'exit' para salir):")

def audio_capture():
	audio = pyaudio.PyAudio()
	stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
	stream.start_stream()
	print("Di algo...")
	while True:
		data = stream.read(4096)
		if recognizer.AcceptWaveform(data):
			result = json.loads(recognizer.Result())
			texto = result['text']
			if texto:
				print(f"Texto reconocido: {texto}")
				traduccion = translator.translate(texto, src='en', dest='es')
				print(f"Traducción: {traduccion.text}")
			return texto

# ▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░▓▒░
def handle_read_file_to_speaker(parts):
	if len(parts) > 1:
		read_file_to_speaker(parts[1])
	else:
		handle_help("read_file_to_speaker")

def handle_check_disk_space(parts):
	if len(parts) > 2:
		check_disk_space(parts[1],parts[2])
	else:
		handle_help("check_disk_space")

def handle_che_if(parts):
	if	che_if(parts[2]) == None:
		handle_help(parts[1])

def handle_cd(parts):
	if len(parts) > 2:
		che_cd(parts[1])
	else:
		handle_help("che_cd")

def handle_md(parts):
	if len(parts) > 2:
		create_directory(parts[1])
	else:
		handle_help("list_directory")

def handle_translate(parts):
	if len(parts) > 2:
		translate_text(parts[1], parts[2], parts[3])
	else:
		print("Uso: traducir <texto> <idioma_origen> <idioma_destino>")

def handle_help(funcion, parametro=None):
	"""
	 Muestra la ayuda para la función especificada, filtrando por parámetro si se proporciona.

	 Parámetros:
	 funcion (callable): La función para la que se desea mostrar la ayuda.
	 parametro (str, opcional): El nombre del parámetro a filtrar en la ayuda.
	 """
	doc = funcion.__doc__

	if parametro:
		# Buscamos si el parámetro está mencionado en la docstring
		if parametro in doc:
			print(doc)
		else:
			print(f"No se encontró información sobre el parámetro '{parametro}' en {funcion.__name__}.")
	else:
		print(doc)
		print(colored(help.__doc__, 'green'))

def handle_date():
	cdate: che_date()
	speak_text("La fecha actual es:" + datetime.datetime())
	print(f"La fecha actual es: ", cdate)

def handle_rm(parts):
	directory_path = parts[1]
	delete_directory(directory_path)
	pass

def handle_ren(parts):
	old_directory_path = parts[1]
	new_directory_path = parts[2]
	speak_text('Renombrando {old_directory_path} a {new_directory_path}')
	rename_directory(old_directory_path, new_directory_path)

def handle_audio():
	verifica_audio()

def handle_dir(parts):
	speak_text('Listando archivos')
	path = '.'
	show_all = False
	detailed = False

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

def handle_typepdf(parts):
	speak_text('Visualizando archivo ')
	try:
		with open(parts[1], "rb") as f:
			reader = PyPDF2.PdfReader(f)
			for page in reader.pages:
				print(page.extract_text())
	except FileNotFoundError:
		print("El archivo no fue encontrado.")
	except Exception as e:
		print(f"Ocurrió un error al leer el PDF: {e}")

def handle_type(parts):
	speak_text('Visualizando archivo')
	archivo = parts[1]
	type_archivo(archivo)

def handle_get_free_space(parts):
	get_free_space(parts[1])

def handle_get_volume_info(parts):
	get_volume_info(parts[1])

def handle_exists(parts):
	directory_path = parts[1]
	che_if(directory_path)

def main():
	"""
	Este es el procedimiento central
	:return:
	"""
	commands = {
		"readtospeaker": handle_read_file_to_speaker,
		"checkdiskspace": handle_check_disk_space,
		"cheif": handle_che_if,
		"cd": handle_cd,
		"chdir": handle_cd,
		"md": handle_md,
		"mkdir": handle_md,
		"rm": handle_rm,
		"rmdir": handle_rm,
		"traducir": handle_translate,
		"help": handle_help,
		"date": handle_date,
		"dir": handle_dir,
		"typepdf": handle_typepdf,
		"type": handle_type,
		"freespace": handle_get_free_space,
		"volumeinfo": handle_get_volume_info,
		"exists": handle_exists
	}

	while True:
		directorio_actual = os.getcwd()
		prompt_text = colored(f"{directorio_actual}>", 'red')
		print(prompt_text, end='')

		t1 = threading.Thread(target=entrada_voz)
		t2 = threading.Thread(target=get_user_input)

		# Iniciamos ambos threads
		t1.start()
		t2.start()

		# Esperamos a que terminen ambos
		t1.join()
		t2.join()
		audio_capture()
		print("Estás en main...voice input:", voice_input)

		user_input = get_user_input()
		parts = user_input.split()

		if len(parts) == 0:
			print("Entrada vacia")
			continue

		command = parts[0].lower()

		if command == "exit" or voice_input.lower() == "exit":
			speak_text("Gracias por utilizar mi aplicación.  ")
			print("Saliendo...")
			break
		elif command in commands:
			commands[command](parts)
		else:
			print("Comando no reconocido. Intenta 'help' para ver los comandos disponibles.")

		if len(parts) >= 1:
			for x in range(len(parts)):
				print(f"{x} {parts[x]}")

if __name__ == "__main__":
	voice_input = ''
	print("Hola! Soy AtomSophy! ¿Cómo estás?, usando PyCharm")
	speak_text("Hola soy AtomSophy, ¿cómo estás?, usando PyCharm")
	main()