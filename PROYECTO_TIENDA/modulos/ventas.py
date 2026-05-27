import os
from datetime import datetime

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import (
    mostrar_titulo,
    mostrar_exito,
    mostrar_error,
    mostrar_alerta,
    pedir_texto,
    pedir_entero,
    confirmar_accion
)
from modulos.clientes import buscar_cliente_por_nit

RUTA_PRODUCTOS = "datos/productos.json"
RUTA_CLIENTES = "datos/clientes.json"
RUTA_VENTAS = "datos/ventas.json"
CARPETA_FACTURAS = "facturas"


def buscar_producto_por_codigo(productos, codigo):
    """Busca un producto por código."""
    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            return producto

    return None


def generar_id_venta(ventas):
    """Genera un ID automático para la venta."""
    numero = len(ventas) + 1
    return f"V{numero:04d}"


def calcular_totales(carrito):
    """Calcula subtotal, IVA y total."""
    subtotal = sum(item["subtotal"] for item in carrito)
    iva = round(subtotal * 0.12, 2)
    total = round(subtotal + iva, 2)

    return round(subtotal, 2), iva, total


def mostrar_carrito(carrito):
    """Muestra los productos agregados al carrito."""
    mostrar_titulo("CARRITO DE COMPRA")

    if not carrito:
        mostrar_alerta("El carrito está vacío.")
        return

    print(f"{'Código':<10} {'Producto':<25} {'Cant.':<8} {'Precio':<10} {'Subtotal':<10}")
    print("-" * 70)

    for item in carrito:
        print(
            f"{item['codigo']:<10} "
            f"{item['nombre']:<25} "
            f"{item['cantidad']:<8} "
            f"Q{item['precio_unit']:<9.2f} "
            f"Q{item['subtotal']:<9.2f}"
        )

    subtotal, iva, total = calcular_totales(carrito)

    print("-" * 70)
    print(f"Subtotal: Q{subtotal:.2f}")
    print(f"IVA 12%:  Q{iva:.2f}")
    print(f"Total:    Q{total:.2f}")


def agregar_producto_carrito(carrito):
    """Agrega un producto al carrito validando stock."""
    productos = cargar_json(RUTA_PRODUCTOS)

    codigo = pedir_texto("Código del producto: ")
    producto = buscar_producto_por_codigo(productos, codigo)

    if not producto:
        mostrar_error("Producto no encontrado.")
        return

    cantidad = pedir_entero("Cantidad: ")

    if cantidad > producto["stock"]:
        mostrar_error("No hay stock suficiente.")
        mostrar_alerta(f"Stock disponible: {producto['stock']}")
        return

    for item in carrito:
        if item["codigo"] == producto["codigo"]:
            nueva_cantidad = item["cantidad"] + cantidad

            if nueva_cantidad > producto["stock"]:
                mostrar_error("No hay stock suficiente para esa cantidad total.")
                return

            item["cantidad"] = nueva_cantidad
            item["subtotal"] = round(item["cantidad"] * item["precio_unit"], 2)
            mostrar_exito("Cantidad actualizada en el carrito.")
            return

    item = {
        "codigo": producto["codigo"],
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio_unit": producto["precio"],
        "subtotal": round(cantidad * producto["precio"], 2)
    }

    carrito.append(item)
    mostrar_exito("Producto agregado al carrito.")


def quitar_producto_carrito(carrito):
    """Quita un producto del carrito."""
    if not carrito:
        mostrar_alerta("El carrito está vacío.")
        return

    codigo = pedir_texto("Código del producto a quitar: ")

    for item in carrito:
        if item["codigo"].lower() == codigo.lower():
            carrito.remove(item)
            mostrar_exito("Producto eliminado del carrito.")
            return

    mostrar_error("Producto no encontrado en el carrito.")


def validar_cliente_venta():
    """Valida NIT del cliente o permite Consumidor Final."""
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
    """Descuenta del inventario los productos vendidos."""
    productos = cargar_json(RUTA_PRODUCTOS)

    for item in carrito:
        producto = buscar_producto_por_codigo(productos, item["codigo"])

        if producto:
            producto["stock"] -= item["cantidad"]

    guardar_json(RUTA_PRODUCTOS, productos)


def crear_factura(venta):
    """Genera una factura en archivo .txt."""
    os.makedirs(CARPETA_FACTURAS, exist_ok=True)

    nombre_archivo = f"{venta['id_venta']}.txt"
    ruta_factura = os.path.join(CARPETA_FACTURAS, nombre_archivo)

    with open(ruta_factura, "w", encoding="utf-8") as archivo:
        archivo.write("======== FACTURA TU TIENDA ========\n")
        archivo.write(f"No. Venta: {venta['id_venta']}\n")
        archivo.write(f"Fecha: {venta['fecha']}\n")
        archivo.write(f"NIT Cliente: {venta['nit_cliente']}\n")
        archivo.write("-----------------------------------\n")

        for item in venta["items"]:
            archivo.write(
                f"{item['nombre']} x{item['cantidad']} "
                f"Q{item['precio_unit']:.2f} = Q{item['subtotal']:.2f}\n"
            )

        archivo.write("-----------------------------------\n")
        archivo.write(f"Subtotal: Q{venta['subtotal']:.2f}\n")
        archivo.write(f"IVA 12%:  Q{venta['iva']:.2f}\n")
        archivo.write(f"Total:    Q{venta['total']:.2f}\n")
        archivo.write("===================================\n")
        archivo.write("Gracias por su compra.\n")

    return ruta_factura


def confirmar_venta(carrito, nit_cliente):
    """Confirma la venta, guarda datos, descuenta stock y genera factura."""
    if not carrito:
        mostrar_error("No se puede confirmar una venta vacía.")
        return False

    ventas = cargar_json(RUTA_VENTAS)
    subtotal, iva, total = calcular_totales(carrito)

    venta = {
        "id_venta": generar_id_venta(ventas),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nit_cliente": nit_cliente,
        "items": carrito.copy(),
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    }

    descontar_stock(carrito)

    ventas.append(venta)
    guardar_json(RUTA_VENTAS, ventas)

    ruta_factura = crear_factura(venta)

    mostrar_exito("Venta confirmada correctamente.")
    mostrar_exito(f"Factura generada: {ruta_factura}")

    return True


def iniciar_venta():
    """Inicia el proceso completo de una nueva venta."""
    mostrar_titulo("NUEVA VENTA")

    nit_cliente = validar_cliente_venta()
    carrito = []

    while True:
        mostrar_titulo("MENÚ DE VENTA")

        print("1. Agregar producto")
        print("2. Mostrar carrito")
        print("3. Quitar producto")
        print("4. Confirmar venta")
        print("5. Cancelar venta")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto_carrito(carrito)

        elif opcion == "2":
            mostrar_carrito(carrito)

        elif opcion == "3":
            quitar_producto_carrito(carrito)

        elif opcion == "4":
            mostrar_carrito(carrito)

            if confirmar_accion("¿Desea confirmar la venta?"):
                realizada = confirmar_venta(carrito, nit_cliente)

                if realizada:
                    break
            else:
                mostrar_alerta("Venta no confirmada.")

        elif opcion == "5":
            if confirmar_accion("¿Desea cancelar la venta?"):
                mostrar_alerta("Venta cancelada. No se modificó el stock.")
                break

        else:
            mostrar_error("Opción inválida.")


def menu_ventas():
    """Muestra el menú del módulo de ventas."""
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