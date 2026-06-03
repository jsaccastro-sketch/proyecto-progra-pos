# carrito.py
# Funciones del carrito de ventas

from modulos.archivos import cargar_json
from modulos.utilidades import (
    mostrar_titulo, mostrar_exito, mostrar_error,
    mostrar_alerta, pedir_texto, pedir_entero
)

RUTA_PRODUCTOS = "datos/productos.json"


def buscar_producto_por_codigo(productos, codigo):
    """Busca un producto por código."""
    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            return producto

    return None


def mostrar_carrito(carrito):
    """Muestra el carrito."""
    mostrar_titulo("CARRITO DE COMPRA")

    if not carrito:
        mostrar_alerta("El carrito está vacío.")
        return

    print(f"{'Código':<10} {'Producto':<25} {'Cant.':<8} {'Precio':<10} {'Subtotal':<10}")
    print("-" * 70)

    for item in carrito:
        print(
            f"{item['codigo']:<10} {item['nombre']:<25} "
            f"{item['cantidad']:<8} Q{item['precio_unit']:<9.2f} "
            f"Q{item['subtotal']:<9.2f}"
        )


def agregar_producto_carrito(carrito):
    """Agrega producto al carrito."""
    productos = cargar_json(RUTA_PRODUCTOS)
    codigo = pedir_texto("Código del producto: ")
    producto = buscar_producto_por_codigo(productos, codigo)

    if not producto:
        mostrar_error("Producto no encontrado.")
        return

    cantidad = pedir_entero("Cantidad: ")

    if not hay_stock(producto, cantidad, carrito):
        return

    agregar_o_actualizar_item(carrito, producto, cantidad)


def hay_stock(producto, cantidad, carrito):
    """Valida stock disponible."""
    cantidad_actual = 0

    for item in carrito:
        if item["codigo"] == producto["codigo"]:
            cantidad_actual = item["cantidad"]

    if cantidad_actual + cantidad > producto["stock"]:
        mostrar_error("No hay stock suficiente.")
        mostrar_alerta(f"Stock disponible: {producto['stock']}")
        return False

    return True


def agregar_o_actualizar_item(carrito, producto, cantidad):
    """Agrega o actualiza un producto."""
    for item in carrito:
        if item["codigo"] == producto["codigo"]:
            item["cantidad"] += cantidad
            item["subtotal"] = round(item["cantidad"] * item["precio_unit"], 2)
            mostrar_exito("Cantidad actualizada en el carrito.")
            return

    carrito.append(crear_item(producto, cantidad))
    mostrar_exito("Producto agregado al carrito.")


def crear_item(producto, cantidad):
    """Crea un item para el carrito."""
    return {
        "codigo": producto["codigo"],
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio_unit": producto["precio"],
        "subtotal": round(cantidad * producto["precio"], 2)
    }


def quitar_producto_carrito(carrito):
    """Quita un producto del carrito."""
    codigo = pedir_texto("Código del producto a quitar: ")

    for item in carrito:
        if item["codigo"].lower() == codigo.lower():
            carrito.remove(item)
            mostrar_exito("Producto eliminado del carrito.")
            return

    mostrar_error("Producto no encontrado en el carrito.")