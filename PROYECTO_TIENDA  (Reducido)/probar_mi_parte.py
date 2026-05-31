# probar_mi_parte.py
# Archivo para probar clientes, ventas, utilidades y JSON

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import (
    mostrar_titulo,
    mostrar_exito,
    mostrar_error,
    mostrar_alerta
)
from modulos.clientes import menu_clientes
from modulos.ventas import menu_ventas


def crear_datos_prueba():
    """Crea productos, clientes y ventas vacías para probar el sistema."""
    productos = [
        {
            "codigo": "P001",
            "nombre": "Azucar 1lb",
            "categoria": "Abarrotes",
            "precio": 6.50,
            "stock": 24,
            "stock_minimo": 5
        },
        {
            "codigo": "P002",
            "nombre": "Arroz 1lb",
            "categoria": "Abarrotes",
            "precio": 5.00,
            "stock": 30,
            "stock_minimo": 5
        },
        {
            "codigo": "P003",
            "nombre": "Leche 1L",
            "categoria": "Lacteos",
            "precio": 12.00,
            "stock": 15,
            "stock_minimo": 3
        }
    ]

    clientes = [
        {
            "nit": "1234567-8",
            "nombre": "Maria Lopez",
            "telefono": "5555-1234",
            "email": "maria@correo.com"
        }
    ]

    guardar_json("datos/productos.json", productos)
    guardar_json("datos/clientes.json", clientes)
    guardar_json("datos/ventas.json", [])

    mostrar_exito("Datos de prueba creados correctamente.")


def probar_archivos_json():
    """Verifica que los archivos JSON carguen correctamente."""
    mostrar_titulo("PRUEBA DE ARCHIVOS JSON")

    productos = cargar_json("datos/productos.json")
    clientes = cargar_json("datos/clientes.json")
    ventas = cargar_json("datos/ventas.json")

    if isinstance(productos, list):
        mostrar_exito("productos.json carga correctamente.")
    else:
        mostrar_error("productos.json tiene error.")

    if isinstance(clientes, list):
        mostrar_exito("clientes.json carga correctamente.")
    else:
        mostrar_error("clientes.json tiene error.")

    if isinstance(ventas, list):
        mostrar_exito("ventas.json carga correctamente.")
    else:
        mostrar_error("ventas.json tiene error.")


def probar_utilidades():
    """Prueba mensajes de utilidades."""
    mostrar_titulo("PRUEBA DE UTILIDADES")

    mostrar_exito("Mensaje de éxito funcionando.")
    mostrar_error("Mensaje de error funcionando.")
    mostrar_alerta("Mensaje de alerta funcionando.")


def mostrar_menu_prueba():
    """Muestra el menú de prueba."""
    mostrar_titulo("PRUEBA DE MI PARTE")

    print("1. Crear datos de prueba")
    print("2. Probar archivos JSON")
    print("3. Probar utilidades")
    print("4. Probar módulo de clientes")
    print("5. Probar módulo de ventas")
    print("0. Salir")


def menu_prueba():
    """Ejecuta el menú para probar los módulos."""
    while True:
        mostrar_menu_prueba()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_datos_prueba()
        elif opcion == "2":
            probar_archivos_json()
        elif opcion == "3":
            probar_utilidades()
        elif opcion == "4":
            menu_clientes()
        elif opcion == "5":
            menu_ventas()
        elif opcion == "0":
            print("Saliendo del programa de prueba...")
            break
        else:
            mostrar_error("Opción inválida.")


menu_prueba()