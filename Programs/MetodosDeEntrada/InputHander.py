class InputHandler:
	def __init__(self):
		self.user_input = None
		self.voice_input = None

	def get_user_input(self):
		# Código para recibir entrada de texto
		pass

	def recognize_speech(self):
		# Código para recibir entrada de voz
		pass

	def interpret_morse(self):
		# Código para interpretar señales de morse
		pass

	def handle_inputs(self):
		# Lógica para priorizar la entrada
		if self.user_input:
			return self.user_input
		elif self.voice_input:
			return self.voice_input
	# Agregar lógica para morse o botones de emergencia
