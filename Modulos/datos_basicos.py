import sys
import time
# Menus y submenus funcion salir
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

def sub_menu_productos():
    print("=" * 35)
    print("      🛒 PRODUCTOS")
    print("=" * 35)
    print(f"  {'[1]':<5} ✨ Agregar Producto")
    print(f"  {'[2]':<5} ❌ Quitar Producto")
    print(f"  {'[3]':<5} 📋 Revisar Inventario")
    print(f"  {'[4]':<5} ⬅️ Volver al Menu Principal")
    print("=" * 35)

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

def salir_del_sistema():

    print("\n👋 ¡Gracias por usar el sistema Gestion Pro!")
    print("Apagando...")
    time.sleep(1)
    sys.exit()


