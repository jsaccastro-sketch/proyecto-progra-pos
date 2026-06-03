"""
Módulo: productos.py
Descripción: Controla el inventario de la tienda.
Autor: Josue Saul Sac Castro 202508101
Fecha: junio 2026
"""

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import (
    mostrar_titulo,
    mostrar_exito,
    mostrar_error,
    mostrar_alerta,
    pedir_texto,
    pedir_entero,
    pedir_float,
    confirmar_accion
)

RUTA_PRODUCTOS = "datos/productos.json"
RUTA_VENTAS = "datos/ventas.json"


def cargar_productos():
    """Abre el archivo JSON y trae la lista con todos los productos."""
    return cargar_json(RUTA_PRODUCTOS)


def guardar_productos(productos):
    """Guarda la lista de productos actualizada en el archivo JSON."""
    guardar_json(RUTA_PRODUCTOS, productos)


def buscar_producto_por_codigo(productos, codigo):
    """Busca un producto por su código exacto. Devuelve el producto o None."""
    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            return producto
    return None


def producto_tiene_ventas(codigo):
    """Revisa en el historial de ventas si este producto ya se vendió antes."""
    ventas = cargar_json(RUTA_VENTAS)
    for venta in ventas:
        for item in venta.get("items", []):
            if item["codigo"].lower() == codigo.lower():
                return True
    return False


def registrar_producto():
    """Pide los datos para meter un producto nuevo al inventario."""
    mostrar_titulo("REGISTRAR PRODUCTO NUEVO")
    productos = cargar_productos()

    codigo = pedir_texto("Código del producto: ")
    if buscar_producto_por_codigo(productos, codigo):
        mostrar_error("Este código de producto ya existe.")
        return

    nombre = pedir_texto("Nombre o descripción: ")
    categoria = pedir_texto("Categoría: ")
    precio = pedir_float("Precio de venta (Q): ")
    
    # Permitir_cero=True por si entran mercancías sin stock inicial
    stock = pedir_entero("Stock inicial: ", permitir_cero=True)
    stock_min = pedir_entero("Stock mínimo de alerta: ", permitir_cero=True)

    nuevo = {
        "codigo": codigo, "nombre": nombre, "categoria": categoria,
        "precio": precio, "stock": stock, "stock_minimo": stock_min
    }

    productos.append(nuevo)
    guardar_productos(productos)
    mostrar_exito("Producto registrado en el sistema.")


def listar_productos():
    """Muestra una tabla con el código, nombre, precio y stock de todo lo que hay."""
    mostrar_titulo("INVENTARIO DE PRODUCTOS")
    productos = cargar_productos()

    if not productos:
        mostrar_alerta("No hay productos registrados en el inventario.")
        return

    print(f"{'Código':<10} {'Nombre':<25} {'Precio':<10} {'Stock':<8}")
    print("-" * 55)

    for prod in productos:
        print(f"{prod['codigo']:<10} {prod['nombre']:<25} Q{prod['precio']:<9.2f} {prod['stock']:<8}")


def buscar_producto():
    """Busca productos escribiendo una parte del código o del nombre."""
    mostrar_titulo("BUSCAR PRODUCTO")
    productos = cargar_productos()
    termino = pedir_texto("Escriba el código o nombre a buscar: ").lower()

    encontrados = []
    for prod in productos:
        if termino in prod["codigo"].lower() or termino in prod["nombre"].lower():
            encontrados.append(prod)

    if not encontrados:
        mostrar_alerta("No se encontró ningún producto.")
        return

    for prod in encontrados:
        print(f"Código: {prod['codigo']} | Nombre: {prod['nombre']}")
        print(f"Categoría: {prod['categoria']} | Precio: Q{prod['precio']:.2f}")
        print(f"Stock Actual: {prod['stock']} | Mínimo: {prod['stock_minimo']}")
        print("-" * 50)


def actualizar_precio():
    """Busca un producto por su código y le cambia el precio de venta."""
    mostrar_titulo("ACTUALIZAR PRECIO")
    productos = cargar_productos()
    codigo = pedir_texto("Ingrese el código del producto: ")

    producto = buscar_producto_por_codigo(productos, codigo)
    if not producto:
        mostrar_error("El producto no existe.")
        return

    print(f"Producto: {producto['nombre']} | Precio actual: Q{producto['precio']:.2f}")
    nuevo_precio = pedir_float("Ingrese el nuevo precio (Q): ")

    producto["precio"] = nuevo_precio
    guardar_productos(productos)
    mostrar_exito("Precio actualizado correctamente.")


def aplicar_ajuste_stock(producto, opcion, cantidad):
    """Función auxiliar para sumar o restar unidades (mide menos de 30 líneas)."""
    if opcion == "1":
        producto["stock"] += cantidad
        mostrar_exito("Stock aumentado por compra/ajuste.")
    elif opcion == "2":
        if cantidad > producto["stock"]:
            mostrar_error("No puedes restar más de lo que hay en existencia.")
            return False
        producto["stock"] -= cantidad
        mostrar_exito("Stock reducido por merma/ajuste.")
    return True


def ajustar_stock():
    """Suma o resta unidades al inventario (por compras, mermas o pérdidas)."""
    mostrar_titulo("AJUSTAR STOCK / EXISTENCIAS")
    productos = cargar_productos()
    codigo = pedir_texto("Ingrese el código del producto: ")

    producto = buscar_producto_por_codigo(productos, codigo)
    if not producto:
        mostrar_error("El producto no existe.")
        return

    print(f"Producto: {producto['nombre']} | Stock actual: {producto['stock']}")
    print("1. Sumar unidades (Compra o Ajuste)\n2. Restar unidades (Merma o Pérdida)")
    opcion = input("Seleccione una opción: ").strip()

    if opcion not in ["1", "2"]:
        mostrar_error("Opción inválida.")
        return

    cantidad = pedir_entero("Cantidad de unidades para ajustar: ")
    
    if aplicar_ajuste_stock(producto, opcion, cantidad):
        guardar_productos(productos)


def eliminar_producto():
    """Borra un producto del JSON si este no se ha vendido nunca en el sistema."""
    mostrar_titulo("ELIMINAR PRODUCTO")
    productos = cargar_productos()
    codigo = pedir_texto("Ingrese el código del producto a borrar: ")

    producto = buscar_producto_por_codigo(productos, codigo)
    if not producto:
        mostrar_error("El producto no existe.")
        return

    if producto_tiene_ventas(codigo):
        mostrar_error("No se puede eliminar porque ya tiene ventas registradas.")
        return

    if confirmar_accion(f"¿Seguro que quiere eliminar '{producto['nombre']}'?"):
        productos.remove(producto)
        guardar_productos(productos)
        mostrar_exito("Producto eliminado del inventario.")
    else:
        mostrar_alerta("Operación cancelada.")


def mostrar_stock_bajo():
    """Muestra una lista  de productos que están bajos en el stock."""
    mostrar_titulo("ALERTA DE STOCK BAJO")
    productos = cargar_productos()
    con_alerta = False

    print(f"{'Código':<10} {'Producto':<25} {'Stock':<8} {'Mínimo':<8}")
    print("-" * 55)

    for prod in productos:
        if prod["stock"] <= prod["stock_minimo"]:
            print(f"{prod['codigo']:<10} {prod['nombre']:<25} {prod['stock']:<8} {prod['stock_minimo']:<8}")
            con_alerta = True

    if not con_alerta:
        print("¡Todo bien! No hay productos con stock bajo en este momento.")


def exportar_productos_csv():

    mostrar_titulo("EXPORTAR INVENTARIO A CSV")
    productos = cargar_productos()

    if not productos:
        mostrar_error("No hay productos para exportar.")
        return

    ruta_csv = "datos/inventario_productos.csv"
    
    try:
        with open(ruta_csv, "w", encoding="utf-8") as archivo:
            
            archivo.write("Codigo,Nombre,Categoria,Precio,Stock,Stock_Minimo\n")
            
            for p in productos:
                archivo.write(
                    f"{p['codigo']},{p['nombre']},{p['categoria']},"
                    f"{p['precio']},{p['stock']},{p['stock_minimo']}\n"
                )
        
        mostrar_exito(f"Inventario guardado en: {ruta_csv}")
        mostrar_alerta("Ya lo puedes abrir en Excel de forma segura.")
        
    except OSError:
        mostrar_error("No se pudo crear el archivo CSV.")


def menu_productos():
    """Menú principal para manejar todas las opciones de este módulo."""
    while True:
        mostrar_titulo("MÓDULO DE PRODUCTOS (INVENTARIO)")
        print("1. Registrar producto nuevo\n2. Listar inventario\n3. Buscar producto")
        print("4. Actualizar precio\n5. Ajustar stock (Entradas/Salidas)")
        print("6. Eliminar producto\n7. Ver alertas de stock bajo")
        print("8. Exportar inventario a Excel (CSV) [Puntos Extra]\n0. Volver")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_precio()
        elif opcion == "5":
            ajustar_stock()
        elif opcion == "6":
            eliminar_producto()
        elif opcion == "7":
            mostrar_stock_bajo()
        elif opcion == "8":
            exportar_productos_csv()
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida.")