def d# ============================================
# devolucion.py
# Sistema POS "Tu Tienda"
# ============================================

from ventas import ventas

# ============================================
# DEVOLUCIÓN
# ============================================

def devolucion():

    print("\n===== DEVOLUCIÓN =====")

    id_venta = input("Ingrese ID de venta: ")

    for venta in ventas:

        if venta["id_venta"] == id_venta:

            print("Venta anulada correctamente")
            return

    print("Venta no encontrada")