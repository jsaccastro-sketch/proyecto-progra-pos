"""
Módulo: reportes.py
Descripción: Administra las estadísticas del negocio, cierres de caja y devoluciones.
Autores: Jose Manuel Lopez Lopez/ 202607037 
Fecha: Mayo 2026
"""

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import (
    mostrar_titulo,
    mostrar_exito,
    mostrar_error,
    mostrar_alerta,
    pedir_texto
)

RUTA_VENTAS = "datos/ventas.json"
RUTA_PRODUCTOS = "datos/productos.json"


def ventas_del_dia():
    """Calcula el total de dinero ingresado y el número de transacciones registradas."""
    mostrar_titulo("VENTAS DEL DÍA")
    ventas = cargar_json(RUTA_VENTAS)

    total = 0
    transacciones = len(ventas)

    for venta in ventas:
        total += venta["total"]

    print(f"Número de transacciones: {transacciones}")
    mostrar_exito(f"Total vendido en el sistema: Q{total:.2f}")


def cierre_caja():
    """Saca las métricas de control diario incluyendo el cálculo del ticket promedio."""
    mostrar_titulo("CIERRE DE CAJA")
    ventas = cargar_json(RUTA_VENTAS)

    total_ventas = 0
    total_productos = 0
    transacciones = len(ventas)

    for venta in ventas:
        total_ventas += venta["total"]
        total_productos += venta.get("cantidad", 0)

    ticket_promedio = total_ventas / transacciones if transacciones > 0 else 0

    print(f"Total de ventas: Q{total_ventas:.2f}")
    print(f"Número de transacciones: {transacciones}")
    print(f"Ticket promedio: Q{round(ticket_promedio, 2):.2f}")
    print(f"Productos vendidos: {total_productos}")
    mostrar_exito("Cierre de caja procesado de forma correcta.")


def regresar_stock_productos(items_devueltos):
    """Función auxiliar para regresar las unidades de la venta anulada al inventario."""
    productos = cargar_json(RUTA_PRODUCTOS)
    for item in items_devueltos:
        for prod in productos:
            if prod["codigo"].lower() == item["codigo"].lower():
                prod["stock"] += item["cantidad"]
    guardar_json(RUTA_PRODUCTOS, productos)


def devolucion():
    """Busca una factura por su ID, la anula y regresa el stock al inventario."""
    mostrar_titulo("DEVOLUCIÓN / ANULACIÓN DE VENTA")
    ventas = cargar_json(RUTA_VENTAS)
    id_venta = pedir_texto("Ingrese el ID de la venta a anular: ")

    for venta in ventas:
        if venta["id_venta"].lower() == id_venta.lower():
            # Si la venta tiene items detallados, les regresamos el stock
            if "items" in venta:
                regresar_stock_productos(venta["items"])
            
            ventas.remove(venta)
            guardar_json(RUTA_VENTAS, ventas)
            mostrar_exito(f"Venta {id_venta.upper()} anulada. Inventario actualizado.")
            return

    mostrar_error("Venta no encontrada en el sistema.")


def menu_reportes():
    """Muestra el panel de control estadístico para el perfil de Administrador."""
    while True:
        mostrar_titulo("MÓDULO DE REPORTES")
        print("1. Ver ventas generales")
        print("2. Procesar cierre de caja")
        print("3. Aplicar devolución de factura")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ventas_del_dia()
        elif opcion == "2":
            cierre_caja()
        elif opcion == "3":
            devolucion()
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida.")