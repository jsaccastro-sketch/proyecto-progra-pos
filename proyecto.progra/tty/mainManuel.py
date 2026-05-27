# ============================================
# main.py
# Sistema POS "Tu Tienda"
# ============================================

from reportes import cierre_caja, devolucion
from ventas import ventas_del_dia

def menu():

    while True:

        print("\n========= SISTEMA POS =========")
        print("1. Ventas del día")
        print("2. Cierre de caja")
        print("3. Devolución")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ventas_del_dia()

        elif opcion == "2":
            cierre_caja()

        elif opcion == "3":
            devolucion()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")

menu()