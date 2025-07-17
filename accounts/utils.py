# Obtener todos los emails de usuarios
def get_emails(users):
    return list(map(lambda u: u.email, users))

# Composición: obtener usernames de usuarios activos
def get_active_usernames(users):
    return list(map(lambda u: u.username, filter(lambda u: u.is_active, users)))
# Funciones utilitarias funcionales para accounts

from functools import reduce

# Ejemplo: función pura para validar email

def is_valid_email(email):
    return "@" in email and "." in email

# Ejemplo: función para filtrar usuarios activos

def filter_active_users(users):
    return list(filter(lambda u: u.is_active, users))

# Ejemplo: función para obtener nombres de usuario

def get_usernames(users):
    return list(map(lambda u: u.username, users))
