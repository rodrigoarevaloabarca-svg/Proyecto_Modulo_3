
user = input("Usuario: ").lower().strip()
password = input("Contraseña: ").lower().strip()

def validar_rut(rut):

    largo = len(rut)
    if 9>= largo >= 8:
        return True
    else:
        return False

def capturar_texto(etiqueta, obligatorio=True):
    while True:
        valor = input(f"{etiqueta}: ").strip()
        if obligatorio and not valor:
            print("❌ Este campo no puede estar vacío.")
            continue
        return valor.lower()

def capturar_rut():
    while True:
        rut = input("RUT (sin puntos ni guion): ").strip().lower()
        if validar_rut(rut):
            return rut
        print("❌ RUT inválido. Debe tener entre 8 y 9 caracteres.")

def capturar_email():
    while True:
        email = input("Email: ").strip().lower()
        if "@" in email and "." in email:
            return email
        print("❌ Formato de email inválido (ej: usuario@correo.com).")

def capturar_producto_nombre():
    while True:
        nombre = input("Nombre del producto: ").lower().strip()
        if nombre:
            return nombre
        print("❌ El nombre no puede estar vacío.")

def capturar_cantidad():
    while True:
        try:
            valor = int(input("Cantidad del producto: "))
            if valor >= 0:
                return valor
            print("❌ La cantidad no puede ser negativa.")
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")

def capturar_precio():
    while True:
        try:
            valor = float(input("Precio del producto: "))
            if valor > 0:
                return valor
            print("❌ El precio debe ser mayor a 0.")
        except ValueError:
            print("❌ Error: Ingrese un precio válido (ej: 1500.50)."