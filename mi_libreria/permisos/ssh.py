# mi_libreria/ssh.py

import paramiko


def ssh_execute_command(host, username, password, command):
	"""
	Función para conectarse a un servidor SSH y ejecutar un comando.

	Parámetros:
	- host: Dirección IP o nombre del servidor.
	- username: Nombre de usuario para SSH.
	- password: Contraseña del usuario SSH.
	- command: Comando a ejecutar en el servidor remoto.

	Retorna:
	- stdout: La salida estándar del comando.
	- stderr: La salida de error del comando, si existe.
	"""
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, username=username, password=password)
		stdin, stdout, stderr = ssh.exec_command(command)
		output = stdout.read().decode()
		error = stderr.read().decode()
		return output, error
	finally:
		ssh.close()


# Ejemplo de uso:
output, error = ssh_execute_command(
	host='ip-del-servidor',
	username='usuario',
	password='tu-contraseña',
	command='ls -l'
)

if error:
	print("Error:", error)
else:
	print("Salida:", output)
def ssh_transfer_file(host, username, password, local_file, remote_file):
    """
    Función para transferir archivos a través de SSH (SCP).

    Parámetros:
    - host: Dirección del servidor SSH.
    - username: Nombre de usuario para SSH.
    - password: Contraseña del usuario SSH.
    - local_file: Ruta del archivo local.
    - remote_file: Ruta del archivo remoto donde se copiará.

    Retorna:
    - None.
    """
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        sftp = ssh.open_sftp()
        sftp.put(local_file, remote_file)
        sftp.close()
    finally:
        ssh.close()

# Ejemplo de uso:
ssh_transfer_file(
    host='ip-del-servidor',
    username='usuario',
    password='tu-contraseña',
    local_file='/ruta/al/archivo-local.txt',
    remote_file='/ruta/remota/al/archivo.txt'
)
