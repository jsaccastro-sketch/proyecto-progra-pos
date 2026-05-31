# facturas.py
# Generación de facturas

import os

CARPETA_FACTURAS = "facturas"


def crear_factura(venta):
    """Genera una factura .txt."""
    os.makedirs(CARPETA_FACTURAS, exist_ok=True)
    ruta = os.path.join(CARPETA_FACTURAS, f"{venta['id_venta']}.txt")

    with open(ruta, "w", encoding="utf-8") as archivo:
        escribir_encabezado(archivo, venta)
        escribir_items(archivo, venta["items"])
        escribir_totales(archivo, venta)

    return ruta


def escribir_encabezado(archivo, venta):
    """Escribe encabezado de factura."""
    archivo.write("======== FACTURA TU TIENDA ========\n")
    archivo.write(f"No. Venta: {venta['id_venta']}\n")
    archivo.write(f"Fecha: {venta['fecha']}\n")
    archivo.write(f"NIT Cliente: {venta['nit_cliente']}\n")
    archivo.write("-----------------------------------\n")


def escribir_items(archivo, items):
    """Escribe productos vendidos."""
    for item in items:
        archivo.write(
            f"{item['nombre']} x{item['cantidad']} "
            f"Q{item['precio_unit']:.2f} = Q{item['subtotal']:.2f}\n"
        )


def escribir_totales(archivo, venta):
    """Escribe totales de factura."""
    archivo.write("-----------------------------------\n")
    archivo.write(f"Subtotal: Q{venta['subtotal']:.2f}\n")
    archivo.write(f"IVA 12%:  Q{venta['iva']:.2f}\n")
    archivo.write(f"Total:    Q{venta['total']:.2f}\n")
    archivo.write("===================================\n")
    archivo.write("Gracias por su compra.\n")