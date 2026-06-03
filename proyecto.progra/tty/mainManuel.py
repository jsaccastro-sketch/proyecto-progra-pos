"""
Módulo: main.py
Descripción: Punto de entrada principal del sistema. Controla el acceso por Login 
             y divide los menús dependiendo de si es Admin o Cajero.
Autor: [Jose Manuel Lopez Lopez/ 202607037] (Integrante 1 - Arquitecto)
Fecha: Mayo 2026
"""

# Importamos los menús de cada módulo usando la ruta correcta
from modulos.utilidades import login, mostrar_titulo, mostrar_error, mostrar_alerta
from modulos.productos import menu_productos
from modulos.clientes import menu_clientes
from modulos.ventas import menu_ventas

# Nota: Dejamos comentada la importación de reportes hasta que tu compañero la programe
from modulos.reportes import menu_reportes


def mostrar_menu_admin():
    """Muestra todas las opciones del sistema para el Administrador."""
    while True:
        mostrar_titulo("MENÚ PRINCIPAL - ADMINISTRADOR")
        print("1. Módulo de Productos (Inventario)")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas / Facturación")
        print("4. Módulo de Reportes y Estadísticas")
        print("0. Cerrar Sesión / Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "0":
            print("Cerrando sesión de administrador...")
            break
        else:
            mostrar_error("Opción inválida.")


def mostrar_menu_cajero():
    """Muestra solo las opciones permitidas para el Cajero (Ventas y Clientes)."""
    while True:
        mostrar_titulo("MENÚ PRINCIPAL - CAJERO")
        print("1. Módulo de Ventas / Facturación")
        print("2. Módulo de Clientes")
        print("0. Cerrar Sesión / Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_ventas()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "0":
            print("Cerrando sesión de cajero...")
            break
        else:
            mostrar_error("Opción inválida.")


def arranque_sistema():
    """Arranca el programa pidiendo Login y desviando al usuario según su rol."""
    # Intentamos loguear al usuario (da 3 intentos adentro de la función)
    rol = login()

    if rol == "admin":
        mostrar_menu_admin()
    elif rol == "cajero":
        mostrar_menu_cajero()
    else:
        mostrar_error("No se pudo iniciar el sistema. Fin del programa.")


# Esto sirve para que el programa corra automáticamente al abrir el archivo
if __name__ == "__main__":
    arranque_sistema()
