from Modulos.gestion_datos import usuario_registrado
from Modulos.datos_basicos import user, password
#login

def login(usuario, contrasena):
    if usuario in usuario_registrado and usuario_registrado[usuario] == contrasena:
        return True
    return False
def sistema_login():
    intentos_maximos = 3
    intentos_actuales = 0
    print("--- SISTEMA DE ACCESO SEGURO ---")
    while intentos_actuales < intentos_maximos:
        print(f"\nIntento {intentos_actuales + 1} de {intentos_maximos}")

        if login(user, password):
            print(f"\n✅ ¡Bienvenido, {user}! Acceso concedido.")
            return True
        else:
            intentos_actuales += 1
            print("❌ Credenciales incorrectas.")
            if intentos_actuales < intentos_maximos:
                print(f"Te quedan {intentos_maximos - intentos_actuales} intentos.")
    print("\n🚫 Acceso bloqueado. Has agotado el número máximo de intentos.")

def validar_rut(rut):

    largo = len(rut)
    if 9>= largo >= 8:
        return True
    else:
        return False




