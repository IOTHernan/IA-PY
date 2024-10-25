# pip install authlib

from authlib.integrations.requests_client import OAuth2Session

# Información del cliente (cliente_id y cliente_secreto obtenidos de la plataforma)
client_id = 'tu-client-id'
client_secret = 'tu-client-secret'
redirect_uri = 'https://tudominio.com/oauth2/callback'  # Redirección luego del login

# URL del proveedor OAuth (por ejemplo, Google o Microsoft)
authorization_endpoint = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_endpoint = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

# Crear una sesión OAuth2
session = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)

# Generar la URL para redirigir al usuario a la página de autenticación
authorization_url, state = session.create_authorization_url(authorization_endpoint)

print("Por favor, visita esta URL para iniciar sesión:", authorization_url)

# El usuario accede y, luego de autenticarse, se te redirige con un "code"
# Ahora intercambiás ese código por un token de acceso:

code = input("Ingresa el código que te dieron en la URL de redirección: ")
token = session.fetch_token(token_endpoint, code=code)

print("Access Token:", token)

# Ahora podés usar este token para hacer peticiones en nombre del usuario:
protected_url = 'https://graph.microsoft.com/v1.0/me'
response = session.get(protected_url)
print("Datos del usuario:", response.json())
