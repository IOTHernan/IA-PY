# test.py

from mi_libreria import oauth2_login, ssh_execute_command, has_permission

# Ejemplo de uso de las funciones
token = oauth2_login('tu-client-id', 'tu-client-secret', 'tu-redirect-uri',
                     'https://auth.endpoint', 'https://token.endpoint')
print("Token de acceso:", token)

user = User('ejemplo', ['read', 'write'])
print("Tiene permiso para escribir:", has_permission(user, 'write'))

output, error = ssh_execute_command('ip-del-servidor', 'usuario', 'contraseña', 'ls -l')
print("Salida SSH:", output)
if error:
    print("Error SSH:", error)
