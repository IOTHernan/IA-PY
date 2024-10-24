# pip install Pillow
import os
import random
import tkinter as tk
from PIL import Image, ImageTk


class Screensaver:
	def __init__(self, root, image_folder):
		self.root = root
		self.root.attributes('-fullscreen', True)  # Pantalla completa
		self.root.bind('<Escape>', self.exit_screensaver)  # Salir con Esc

		self.image_folder = image_folder
		self.images = self.load_images()
		self.current_image = None

		self.show_random_image()

	def load_images(self):
		# Cargar imágenes del directorio
		image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
		return [os.path.join(self.image_folder, f) for f in image_files]

	def show_random_image(self):
		# Mostrar una imagen aleatoria
		if self.images:
			image_path = random.choice(self.images)
			image = Image.open(image_path)

			# Ajustar imagen a la pantalla
			screen_width = self.root.winfo_screenwidth()
			screen_height = self.root.winfo_screenheight()
			image = image.resize((screen_width, screen_height), Image.ANTIALIAS)

			self.current_image = ImageTk.PhotoImage(image)
			label = tk.Label(self.root, image=self.current_image)
			label.place(relwidth=1, relheight=1)

		self.root.after(5000, self.show_random_image)  # Cambiar imagen cada 5 segundos

	def exit_screensaver(self, event):
		self.root.quit()


if __name__ == "__main__":
	root = tk.Tk()
	image_folder = "ruta/a/tu/directorio/de/imágenes"  # Cambia esto a tu ruta
	screensaver = Screensaver(root, image_folder)
	root.mainloop()
