import time
from Modulos.datos_basicos import salir_del_sistema,menu_principal
from Modulos.gestion_datos import seccion_clientes,seccion_productos,seccion_ventas,exportar_resumen_csv, sistema_login

def iniciar_sesion():
    acceso_concedido = sistema_login()
    if not acceso_concedido:
        print("\n🔒 Sistema bloqueado contacta a soporte.")
        return

    menu_opciones = {
        "1":seccion_clientes,
        "2":seccion_productos,
        "3":seccion_ventas,
        "4":exportar_resumen_csv,
        "5": salir_del_sistema
    }

    while True:
        menu_principal()
        eleccion = input(">> Ingrese el número de su opción: ")

        if eleccion in menu_opciones:
            funcion_a_ejecutar = menu_opciones[eleccion]
            funcion_a_ejecutar()
        else:
            print("\n🚫 Opción no válida. Intente con 1, 2, 3 o 4.")
            time.sleep(1)
if __name__ == "__main__":
    iniciar_sesion()
