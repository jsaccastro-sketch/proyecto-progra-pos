# ventas.py
# Menú y flujo principal de ventas

from modulos.utilidades import mostrar_titulo, mostrar_error, mostrar_alerta, confirmar_accion
from modulos.carrito import (
    agregar_producto_carrito, mostrar_carrito, quitar_producto_carrito
)
from modulos.ventas_servicio import validar_cliente_venta, confirmar_venta


def iniciar_venta():
    """Inicia una nueva venta."""
    mostrar_titulo("NUEVA VENTA")
    nit_cliente = validar_cliente_venta()
    carrito = []

    while True:
        mostrar_menu_venta()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto_carrito(carrito)
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            quitar_producto_carrito(carrito)
        elif opcion == "4":
            procesar_confirmacion(carrito, nit_cliente)
            break
        elif opcion == "5":
            if cancelar_venta():
                break
        else:
            mostrar_error("Opción inválida.")


def mostrar_menu_venta():
    """Muestra opciones de venta."""
    mostrar_titulo("MENÚ DE VENTA")
    print("1. Agregar producto")
    print("2. Mostrar carrito")
    print("3. Quitar producto")
    print("4. Confirmar venta")
    print("5. Cancelar venta")


def procesar_confirmacion(carrito, nit_cliente):
    """Procesa confirmación de venta."""
    mostrar_carrito(carrito)

    if confirmar_accion("¿Desea confirmar la venta?"):
        confirmar_venta(carrito, nit_cliente)
    else:
        mostrar_alerta("Venta no confirmada.")


def cancelar_venta():
    """Cancela la venta."""
    if confirmar_accion("¿Desea cancelar la venta?"):
        mostrar_alerta("Venta cancelada. No se modificó el stock.")
        return True

    return False


def menu_ventas():
    """Muestra menú de ventas."""
    while True:
        mostrar_titulo("MÓDULO DE VENTAS")

        print("1. Iniciar nueva venta")
        print("0. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            iniciar_venta()
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida.")