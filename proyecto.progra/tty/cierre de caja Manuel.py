# ============================================
# cierre_caja.py
# Sistema POS "Tu Tienda"
# ============================================

from ventas import ventas

# ============================================
# CIERRE DE CAJA
# ============================================

def cierre_caja():

    print("\n===== CIERRE DE CAJA =====")

    total_ventas = 0
    total_productos = 0
    transacciones = len(ventas)

    for venta in ventas:

        total_ventas += venta["total"]
        total_productos += venta["cantidad"]

    if transacciones > 0:
        ticket_promedio = total_ventas / transacciones
    else:
        ticket_promedio = 0

    print("Total de ventas: Q", total_ventas)
    print("Número de transacciones:", transacciones)
    print("Ticket promedio: Q", round(ticket_promedio, 2))
    print("Productos vendidos:", total_productos)