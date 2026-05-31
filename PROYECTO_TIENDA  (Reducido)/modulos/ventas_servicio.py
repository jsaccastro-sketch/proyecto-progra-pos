# ventas_servicio.py
# Servicios principales de ventas

from datetime import datetime

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import mostrar_exito, mostrar_error, mostrar_alerta, pedir_texto
from modulos.clientes_busqueda import buscar_cliente_por_nit
from modulos.carrito import buscar_producto_por_codigo
from modulos.facturas import crear_factura

RUTA_PRODUCTOS = "datos/productos.json"
RUTA_CLIENTES = "datos/clientes.json"
RUTA_VENTAS = "datos/ventas.json"


def generar_id_venta(ventas):
    """Genera ID de venta."""
    return f"V{len(ventas) + 1:04d}"


def calcular_totales(carrito):
    """Calcula subtotal, IVA y total."""
    subtotal = round(sum(item["subtotal"] for item in carrito), 2)
    iva = round(subtotal * 0.12, 2)
    total = round(subtotal + iva, 2)

    return subtotal, iva, total


def validar_cliente_venta():
    """Valida cliente o usa CF."""
    clientes = cargar_json(RUTA_CLIENTES)
    nit = pedir_texto("Ingrese NIT del cliente o CF: ")

    if nit.upper() == "CF":
        return "CF"

    cliente = buscar_cliente_por_nit(clientes, nit)

    if cliente:
        mostrar_exito(f"Cliente encontrado: {cliente['nombre']}")
        return cliente["nit"]

    mostrar_alerta("Cliente no registrado. Se usará Consumidor Final.")
    return "CF"


def descontar_stock(carrito):
    """Descuenta stock de productos."""
    productos = cargar_json(RUTA_PRODUCTOS)

    for item in carrito:
        producto = buscar_producto_por_codigo(productos, item["codigo"])

        if producto:
            producto["stock"] -= item["cantidad"]

    guardar_json(RUTA_PRODUCTOS, productos)


def crear_objeto_venta(carrito, nit_cliente, ventas):
    """Crea el diccionario de venta."""
    subtotal, iva, total = calcular_totales(carrito)

    return {
        "id_venta": generar_id_venta(ventas),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nit_cliente": nit_cliente,
        "items": carrito.copy(),
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    }


def confirmar_venta(carrito, nit_cliente):
    """Confirma y guarda una venta."""
    if not carrito:
        mostrar_error("No se puede confirmar una venta vacía.")
        return False

    ventas = cargar_json(RUTA_VENTAS)
    venta = crear_objeto_venta(carrito, nit_cliente, ventas)

    descontar_stock(carrito)
    ventas.append(venta)
    guardar_json(RUTA_VENTAS, ventas)

    ruta_factura = crear_factura(venta)
    mostrar_exito("Venta confirmada correctamente.")
    mostrar_exito(f"Factura generada: {ruta_factura}")

    return True