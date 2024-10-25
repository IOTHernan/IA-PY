# pip install pocketsphinx
# pip install vosk
#

import pyttsx3
from google.cloud import translate
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import googletrans
import json
import pyaudio
# Configurar el modelo de Vosk
model = Model("C:/ChipSoft/Python/vosk/vosk-model-es-0.42/vosk-model-es-0.42")
recognizer = KaldiRecognizer(model, 16000)

# Configurar Googletrans
translator = googletrans.Translator()

def speak_text(text):
    """Función para sintetizar y reproducir voz a partir de texto."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# @memory_monitor
def translate_text(text, src='en', dest='es'):
    """
    Traduce un texto.
    :param text:
    :param src:
    :param dest:
    :return:
    """
    translator = Translator()
    return translator.translate(text, src=src, dest=dest).text


def translate_text_gcp(text, target='es'):
    """Función para traducir texto usando Google Cloud Translate."""
    client = translate.Client()
    result = client.translate(text, target_language=target)
    return result['translatedText']


def read_file_to_speaker(file_path):
    """

    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            speak_text(file.read())

    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None