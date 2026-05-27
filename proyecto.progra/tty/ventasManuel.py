# ============================================
# ventas.py
# Sistema POS "Tu Tienda"
# ============================================

ventas = [

    {
        "id_venta": "V001",
        "fecha": "2026-05-20",
        "cliente": "CF",
        "cantidad": 3,
        "total": 45.00
    },

    {
        "id_venta": "V002",
        "fecha": "2026-05-20",
        "cliente": "1234567-8",
        "cantidad": 2,
        "total": 30.00
    }
]

# ============================================
# VENTAS DEL DÍA
# ============================================

def ventas_del_dia():

    print("\n===== VENTAS DEL DÍA =====")

    total = 0
    transacciones = 0

    for venta in ventas:

        total += venta["total"]
        transacciones += 1

    print("Transacciones:", transacciones)
    print("Total vendido: Q", total)