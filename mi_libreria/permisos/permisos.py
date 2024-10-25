# mi_libreria/permisos.py

class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

def has_permission(user, permission):
    """
    Verifica si un usuario tiene un permiso específico.

    Parámetros:
    - user: Instancia de la clase User.
    - permission: Permiso a verificar.

    Retorna:
    - True si el usuario tiene el permiso, False en caso contrario.
    """
    return permission in user.permissions

# Ejemplo de uso:
#user = User('juanp', ['read', 'write', 'delete'])
#print(has_permission(user, 'write'))  # Debería retornar True
#print(has_permission(user, 'execute'))  # Debería retornar False


def assign_permission(user, permission):
    """
    Asigna un permiso a un usuario.

    Parámetros:
    - user: Instancia de la clase User.
    - permission: Permiso a asignar.

    Retorna:
    - None.
    """
    if permission not in user.permissions:
        user.permissions.append(permission)

# Ejemplo de uso:
#assign_permission(user, 'execute')
#print(user.permissions)  # ['read', 'write', 'delete', 'execute']


def revoke_permission(user, permission):
    """
    Revoca un permiso de un usuario.

    Parámetros:
    - user: Instancia de la clase User.
    - permission: Permiso a revocar.

    Retorna:
    - None.
    """
    if permission in user.permissions:
        user.permissions.remove(permission)

# Ejemplo de uso:
#revoke_permission(user, 'delete')
#print(user.permissions)  # ['read', 'write', 'execute']


def can_access_resource(user, resource):
    """
    Verifica si un usuario puede acceder a un recurso basado en sus permisos.

    Parámetros:
    - user: Instancia de la clase User.
    - resource: Recurso al que se quiere acceder.

    Retorna:
    - True si el usuario tiene permiso para acceder, False en caso contrario.
    """
    resource_permissions = {
        'documento_privado': ['read', 'write'],
        'documento_publico': ['read'],
        'documento_confidencial': ['read', 'write', 'delete']
    }

    required_permissions = resource_permissions.get(resource, [])
    return all(has_permission(user, perm) for perm in required_permissions)

# Ejemplo de uso:
#print(can_access_resource(user, 'documento_privado'))  # Debería retornar True
#print(can_access_resource(user, 'documento_confidencial'))  # Debería retornar False
