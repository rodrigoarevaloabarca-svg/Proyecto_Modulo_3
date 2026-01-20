#login
usuario_registrado = {
    "admin" : "123456",
    "invitado" : "123456",
    "1":"1"
}
def login(usuario, contrasena):
    if usuario in usuario_registrado and usuario_registrado[usuario] == contrasena:
        return True
    return False

def validar_rut(rut):

    largo = len(rut)
    if 9>= largo >= 8:
        return True
    else:
        return False




