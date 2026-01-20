from Modulos.funciones_utiles import ingresar_cliente,eliminar_cliente,buscar_cliente,ingresar_producto,eliminar_producto,revisar_inventario,ventas,cancelar_venta,resumen_ventas,ver_cancelaciones
def menu_principal():
    print("=" * 35)
    print("      🚀 SISTEMA DE GESTIÓN PRO")
    print("=" * 35)
    print(f"  {'[1]':<5} 👤 Gestion Clientes")
    print(f"  {'[2]':<5} 🗑️ Gestion Productos")
    print(f"  {'[3]':<5} 💰 Ventas")
    print(f"  {'[4]':<5} 📦 Resumen Diario Exportable")
    print(f"  {'[5]':<5} 🚪 Salir")
    print("=" * 35)

def sub_menu_clientes ():
    print("=" * 35)
    print("      🚀 CLIENTES")
    print("=" * 35)
    print(f"  {'[1]':<5} 👤 Agregar Cliente")
    print(f"  {'[2]':<5} 🗑️ Quitar Cliente")
    print(f"  {'[3]':<5} 📦 Buscar Cliente")
    print(f"  {'[4]':<5} ⬅️ Volver al Menu Principal")
    print("=" * 35)

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

def sub_menu_productos():
    print("=" * 35)
    print("      🛒 PRODUCTOS")
    print("=" * 35)
    print(f"  {'[1]':<5} ✨ Agregar Producto")
    print(f"  {'[2]':<5} ❌ Quitar Producto")
    print(f"  {'[3]':<5} 📋 Revisar Inventario")
    print(f"  {'[4]':<5} ⬅️ Volver al Menu Principal")
    print("=" * 35)
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

def sub_menu_ventas():
    print("=" * 35)
    print("      🛒 VENTAS")
    print("=" * 35)
    print(f"  {'[1]':<5} ➕ Ventas")
    print(f"  {'[2]':<5} 🚫 cancelar venta")
    print(f"  {'[3]':<5} 📑 Ventas Realizadas")
    print(f"  {'[4]':<5} ❌ Ventas Canceladas")
    print(f"  {'[5]':<5} ⬅️ Volver al Menu Principal")
    print("=" * 35)
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

