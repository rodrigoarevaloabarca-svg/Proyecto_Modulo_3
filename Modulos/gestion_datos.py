import datetime
import csv
from Modulos.datos_basicos import sub_menu_clientes,sub_menu_productos,sub_menu_ventas
from Modulos.validaciones import validar_rut,login
#login
def sistema_login():
    intentos_maximos = 3
    intentos_actuales = 0
    print("--- SISTEMA DE ACCESO SEGURO ---")
    while intentos_actuales < intentos_maximos:
        print(f"\nIntento {intentos_actuales + 1} de {intentos_maximos}")
        user = input("Usuario: ").lower().strip()
        password = input("Contraseña: ").lower().strip()
        if login(user, password):
            print(f"\n✅ ¡Bienvenido, {user}! Acceso concedido.")
            return True
        else:
            intentos_actuales += 1
            print("❌ Credenciales incorrectas.")
            if intentos_actuales < intentos_maximos:
                print(f"Te quedan {intentos_maximos - intentos_actuales} intentos.")
    print("\n🚫 Acceso bloqueado. Has agotado el número máximo de intentos.")

#gestion clientes
clientes = {}
def ver_lista_clientes():
    print("\n--- Lista de Clientes Registrados ---")
    if not clientes:
        print("No hay clientes registrados en el sistema.")
    else:
        print(f"{'RUT':<12} | {'Nombre':<25} | {'Email':<30}")
        print("-" * 70)
        for rut, info in clientes.items():
            nombre = info["nombre"].title()
            email = info["email"]
            print(f"{rut:<12} | {nombre:<25} | {email:<30}")
def buscar_cliente():
    print("\n--- Buscar Cliente ---")
    ver_lista_clientes()
    while True:
        rut = input("Rut (sin puntos ni guion): ").lower().strip()
        if validar_rut(rut):
            break
        else:
            print("❌ RUT inválido. Debe tener entre 8 y 9 caracteres. Intente de nuevo.")
    if rut in clientes :
        print("cliente encontrado")
        cliente = clientes[rut]
        print(f"Nombre: {cliente['nombre']}")
        print(f"Email: {cliente['email']}")
    else:
        print("cliente no encontrado")

def ingresar_cliente():
    print("\n--- Registro de Cliente ---")
    nombre = input("Nombre: ").lower().strip()
    while True:
        rut = input("Rut (sin puntos ni guion): ").lower().strip()
        if validar_rut(rut) and rut not in clientes:
            break
        else:
            print("❌ RUT inválido. Debe tener entre 8 y 9 caracteres. Intente de nuevo.")
            print(f"⚠️ El RUT {rut} ya está registrado. Intente con otro.")

    email = input("Email: ").lower().strip()
    clientes[rut] = {
        "nombre": nombre,
        "email": email
    }
    print(f"✅ Cliente {nombre} registrado con éxito.")

def eliminar_cliente():
    print("\n--- Eliminar Cliente ---")
    ver_lista_clientes()

    rut = input("Ingrese el RUT del cliente a eliminar: ").lower().strip()
    if rut in clientes:
        nombre_borrado = clientes[rut]["nombre"]
        clientes.pop(rut)
        print(f"🗑️ El cliente {nombre_borrado} ha sido eliminado.")
    else:
        print("❌ Error: No se encontró ningún cliente con ese RUT.")

def seccion_clientes():
    opciones_clientes = {
        "1": ingresar_cliente,
        "2": eliminar_cliente,
        "3": buscar_cliente,
    }
    while True:
        sub_menu_clientes()
        eleccion_cliente = input(">> Ingrese el número de su opción: ")
        if eleccion_cliente == "4":
            print("Regresando al menú principal...")
            break
        if eleccion_cliente in opciones_clientes:
            funcion_cliente = opciones_clientes[eleccion_cliente]
            funcion_cliente()
        else:
            print("\n🚫 Opción no válida. Intente con 1, 2, 3, O 4")

#productos
productos = {
    "pc":{
        "stock" : 100,
        "precio" : 1000
    },
    "teclado":{
        "stock" : 100,
        "precio" : 100
    },
    "mouse":{
        "stock" : 100,
        "precio" : 50
    }

}
def ingresar_producto():
    print("\n--- Registro de Producto ---")
    nombre_producto = input("Nombre del producto: ").lower().strip()
    cantidad_producto = int(input("Cantidad del producto: "))
    precio_producto = float(input("Precio del producto: "))
    productos [ nombre_producto ] = {
        "stock":cantidad_producto,
        "precio":precio_producto
    }
def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    nombre_producto = input("Nombre del producto: ").lower().strip()
    if nombre_producto in productos :
        productos.pop(nombre_producto)
        print(f"el producto {nombre_producto} ha sido eliminado.")

def revisar_inventario():
    print("\n--- Revisar Inventario ---")
    if not productos:
        print("El inventario está vacío.")
    else:
        print(f"{'Producto':<20} | {'Stock':<10} | {'Precio':<10}")
        print("-" * 45)
        for nombre, info in productos.items():
            stock = info["stock"]
            precio = info["precio"]
            print(f"{nombre.capitalize():<20} | {stock:<10} | ${precio:<10.2f}")

def seccion_productos():
    opciones_productos = {
        "1": ingresar_producto,
        "2": eliminar_producto,
        "3": revisar_inventario,
    }
    while True:
        sub_menu_productos()
        eleccion_producto = input(">> Ingrese el número de su opción: ")
        if eleccion_producto == "4":
            print("Regresando al menú principal...")
            break
        if eleccion_producto in opciones_productos:
            funcion_productos = opciones_productos[eleccion_producto]
            funcion_productos()
        else:
            print("\n🚫 Opción no válida. Intente con 1, 2, 3, O 4")

#Ventas
ventas_realizadas = {}
contador_ventas = 1

def ventas():
    global contador_ventas
    print("--- Ventas ---")
    descuento = 1.0
    cliente_nombre = "Consumidor Final"
    rut_cliente = input("Ingrese RUT del cliente para descuento (o Enter para saltar): ").lower().strip()
    if rut_cliente in clientes:
        descuento = 0.9
        cliente_nombre = clientes[rut_cliente]["nombre"].title()
        print(f"✨ ¡Cliente registrado! Se aplicará un 10% de descuento a {cliente_nombre}.")
    else:
        print("💡 Cliente no registrado. Venta sin descuento.")
    comprando = True

    while comprando:
        revisar_inventario()
        ingresa_producto = input("\nIngrese el nombre del producto (o 'fin' para terminar): ").lower().strip()

        if ingresa_producto == 'fin':
            break

        if ingresa_producto in productos:
            try:
                ingresa_cantidad = int(input(f"¿Cuántas unidades de '{ingresa_producto}'?: "))
                stock_actual = productos[ingresa_producto]["stock"]

                if stock_actual >= ingresa_cantidad:
                    precio_unitario = productos[ingresa_producto]["precio"]
                    total_item = (precio_unitario * ingresa_cantidad) * descuento
                    productos[ingresa_producto]["stock"] -= ingresa_cantidad
                    id_venta = f"V{contador_ventas}"
                    ventas_realizadas[id_venta] = {
                        "producto": ingresa_producto,
                        "cantidad": ingresa_cantidad,
                        "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "precio": total_item,
                        "cliente": cliente_nombre
                    }
                    contador_ventas += 1
                    print(f"✅ Agregado: {ingresa_cantidad} de {ingresa_producto}. Total: ${total_item:.2f}")
                else:
                    print(f"❌ Error: Solo quedan {stock_actual} unidades.")
            except ValueError:
                print("❌ Error: Ingrese un número válido.")
        else:
            print("❌ El producto no existe en el inventario.")
        continuar = input("\n¿Desea agregar otro producto a esta venta? (s/n): ").lower().strip()
        if continuar != 's':
            comprando = False

    print("--- Venta finalizada con éxito ---")

def resumen_ventas():
    print("--- Resumen de Ventas ---")
    if not ventas_realizadas:
        print("No hay ventas registradas.")
    else:
        print(f"{'ID':<5} | {'FECHA':<17} | {'PRODUCTO':<15} | {'CANTIDAD':<8} | {'PRECIO':<10} ")
        print("-" * 60)
        for id_venta, info in ventas_realizadas.items():
            fecha = info["fecha"]
            producto = info["producto"]
            cantidad = info["cantidad"]
            precio = info["precio"]
            print(f"{id_venta:<5} | {fecha:<17} | {producto:<15} | {cantidad:<8} | {precio:<10}")

ventas_canceladas = []

def cancelar_venta():
    print("\n--- Cancelar Venta ---")
    if not ventas_realizadas:
        print("No hay ventas registradas para cancelar.")
        return

    resumen_ventas()

    id_busqueda = input("Ingrese el ID de la venta a cancelar (ej. V1): ").strip().upper()
    venta_extraida = ventas_realizadas.pop(id_busqueda, None)
    if venta_extraida:
        nombre_prod = venta_extraida["producto"]
        cantidad_vendida = venta_extraida["cantidad"]

        if nombre_prod in productos:
            productos[nombre_prod]["stock"] += cantidad_vendida
            print(f"✅ Stock actualizado: +{cantidad_vendida} unidades a '{nombre_prod}'.")
        else:
            print(f"⚠️ Aviso: El producto '{nombre_prod}' ya no está en el inventario activo.")

        venta_extraida["id_original"] = id_busqueda
        venta_extraida["motivo"] = "Cancelación de usuario"

        ventas_canceladas.append(venta_extraida)

        print(f"🗑️  La venta {id_busqueda} ha sido movida al historial de cancelaciones.")
    else:
        print(f"❌ Error: El ID '{id_busqueda}' no fue encontrado.")


def ver_cancelaciones():
    print("\n--- Historial de Ventas Canceladas ---")
    if not ventas_canceladas:
        print("No hay registros de cancelaciones.")
    else:
        for v in ventas_canceladas:
            print(f"ID: {v['id_original']} | Producto: {v['producto']} | Total devuelto: ${v['total']}")

def seccion_ventas():
    opciones_ventas = {
        "1": ventas,
        "2": cancelar_venta,
        "3": resumen_ventas,
        "4": ver_cancelaciones
    }
    while True:
        sub_menu_ventas()
        eleccion_producto = input(">> Ingrese el número de su opción: ")
        if eleccion_producto == "5":
            print("Regresando al menú principal...")
            break
        if eleccion_producto in opciones_ventas:
            funcion_productos = opciones_ventas[eleccion_producto]
            funcion_productos()
        else:
            print("\n🚫 Opción no válida. Intente con 1, 2, 3, 4, O 5")
def total_ventas():
    total = 0
    for v in ventas_realizadas.values():
        total += v["precio"]
    return total

#resumen exportable
def exportar_resumen_csv():
    nombre_archivo = f"resumen_movimientos_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    campos = ["ID", "Fecha/Hora", "Tipo Movimiento", "Producto", "Cantidad", "Total/Precio"]

    total_general = total_ventas()

    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for id_v, info in ventas_realizadas.items():
                escritor.writerow({
                    "ID": id_v,
                    "Fecha/Hora": info["fecha"],
                    "Tipo Movimiento": "VENTA",
                    "Producto": info["producto"],
                    "Cantidad": info["cantidad"],
                    "Total/Precio": info["precio"]
                })

            for v_canc in ventas_canceladas:
                escritor.writerow({
                    "ID": v_canc.get("id_original", "N/A"),
                    "Fecha/Hora": v_canc["fecha"],
                    "Tipo Movimiento": "CANCELACION",
                    "Producto": v_canc["producto"],
                    "Cantidad": v_canc["cantidad"],
                    "Total/Precio": v_canc["precio"]
                })

            escritor.writerow({campo: "---" for campo in campos})
            for nombre, info in productos.items():
                escritor.writerow({
                    "ID": "STOCK",
                    "Fecha/Hora": datetime.datetime.now().strftime("%d/%m/%Y"),
                    "Tipo Movimiento": "INVENTARIO ACTUAL",
                    "Producto": nombre.capitalize(),
                    "Cantidad": info["stock"],
                    "Total/Precio": info["precio"]
                })

            escritor.writerow({campo: "" for campo in campos})
            escritor.writerow({
                "ID": "",
                "Fecha/Hora": "",
                "Tipo Movimiento": "",
                "Producto": "",
                "Cantidad": "TOTAL GENERAL VENTAS:",
                "Total/Precio": total_general
            })

        print(f"✅ Reporte exportado exitosamente: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al exportar: {e}")