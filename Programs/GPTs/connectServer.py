# pip install paramiko

import paramiko

# Crear un cliente SSH
ssh = paramiko.SSHClient()

# Cargar las claves de host conocidas
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectarse al servidor
ssh.connect('ip-del-servidor', username='usuario', password='tu-contraseña')

# Ejecutar un comando en el servidor remoto
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())

# Cerrar la conexión
ssh.close()
