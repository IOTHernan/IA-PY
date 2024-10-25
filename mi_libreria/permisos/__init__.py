# mi_libreria/__init__.py
# pip install authlib
# pip install paramiko

from .oauth import oauth2_login, verify_token
from .ssh import ssh_execute_command, ssh_transfer_file
from .permisos import has_permission, assign_permission, revoke_permission, can_access_resource

__all__ = [
    'oauth2_login', # oauth.py
    'verify_token', # oauth.py
    'ssh_execute_command', # ssh.py
    'ssh_transfer_file', # ssh.py
    'has_permission', # permisos.py
    'assign_permission', # permisos.py
    'revoke_permission', # permisos.py
    'can_access_resource' # permisos.py
]
