from modulos.utilidades import mostrar_titulo, mostrar_exito, mostrar_error, mostrar_alerta
from modulos.clientes import menu_clientes
from modulos.ventas import menu_ventas


def probar_utilidades():
    """Prueba mensajes básicos del módulo utilidades."""
    mostrar_titulo("PRUEBA DE UTILIDADES")
    mostrar_exito("Este es un mensaje de éxito.")
    mostrar_error("Este es un mensaje de error.")
    mostrar_alerta("Este es un mensaje de alerta.")


def menu_prueba():
    """Menú para probar los módulos de mi parte."""
    while True:
        mostrar_titulo("PRUEBA DE MI PARTE")

        print("1. Probar utilidades")
        print("2. Probar módulo de clientes")
        print("3. Probar módulo de ventas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            probar_utilidades()

        elif opcion == "2":
            menu_clientes()

        elif opcion == "3":
            menu_ventas()

        elif opcion == "0":
            print("Saliendo del programa de prueba...")
            break

        else:
            mostrar_error("Opción inválida.")


menu_prueba()