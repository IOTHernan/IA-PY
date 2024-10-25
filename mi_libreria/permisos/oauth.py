# mi_libreria/oauth.py

from authlib.integrations.requests_client import OAuth2Session


def oauth2_login(client_id, client_secret, redirect_uri, auth_endpoint, token_endpoint):
	"""
	Función para manejar el flujo de OAuth2.

	Parámetros:
	- client_id: ID de cliente de OAuth2.
	- client_secret: Secreto de cliente de OAuth2.
	- redirect_uri: URI de redirección tras autenticación.
	- auth_endpoint: URL del proveedor de OAuth2 para la autenticación.
	- token_endpoint: URL del proveedor para obtener el token.

	Retorna:
	- access_token: El token de acceso obtenido.
	"""
	session = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)
	authorization_url, state = session.create_authorization_url(auth_endpoint)

	print("Visita esta URL para iniciar sesión:", authorization_url)

	code = input("Ingresa el código de la URL: ")
	token = session.fetch_token(token_endpoint, code=code)

	return token['access_token']


# Ejemplo de uso:
# token = oauth2_login(
# 	client_id='tu-client-id',
# 	client_secret='tu-client-secret',
# 	redirect_uri='https://tu-redirect-uri.com',
# 	auth_endpoint='https://login.microsoftonline.com/common/oauth2/v2.0/authorize',
# 	token_endpoint='https://login.microsoftonline.com/common/oauth2/v2.0/token'
# )
# print("Access Token:", token)


def verify_token(session, protected_url, access_token):
	"""
	Función para verificar si un token de acceso OAuth2 sigue siendo válido.

	Parámetros:
	- session: Instancia de OAuth2Session.
	- protected_url: URL protegida a la que se hace la solicitud.
	- access_token: Token de acceso que se verifica.

	Retorna:
	- response_data: La respuesta de la API si el token es válido.
	"""
	headers = {'Authorization': f'Bearer {access_token}'}
	response = session.get(protected_url, headers=headers)

	if response.status_code == 200:
		return response.json()
	else:
		return None
