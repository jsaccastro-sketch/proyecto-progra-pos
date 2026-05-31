# clientes_busqueda.py
# Búsqueda y listado de clientes

from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import mostrar_titulo, mostrar_alerta, pedir_texto

RUTA_CLIENTES = "datos/clientes.json"


def cargar_clientes():
    """Carga clientes desde JSON."""
    return cargar_json(RUTA_CLIENTES)


def guardar_clientes(clientes):
    """Guarda clientes en JSON."""
    guardar_json(RUTA_CLIENTES, clientes)


def buscar_cliente_por_nit(clientes, nit):
    """Busca un cliente por NIT."""
    for cliente in clientes:
        if cliente["nit"].lower() == nit.lower():
            return cliente
    return None


def listar_clientes():
    """Lista todos los clientes."""
    mostrar_titulo("LISTA DE CLIENTES")
    clientes = cargar_clientes()

    if not clientes:
        mostrar_alerta("No hay clientes registrados.")
        return

    print(f"{'NIT':<15} {'Nombre':<25} {'Teléfono':<15} {'Email':<30}")
    print("-" * 90)

    for cliente in clientes:
        print(
            f"{cliente['nit']:<15} "
            f"{cliente['nombre']:<25} "
            f"{cliente['telefono']:<15} "
            f"{cliente['email']:<30}"
        )


def buscar_cliente():
    """Busca clientes por NIT o nombre."""
    mostrar_titulo("BUSCAR CLIENTE")
    clientes = cargar_clientes()
    termino = pedir_texto("Ingrese NIT o nombre: ").lower()

    encontrados = [
        c for c in clientes
        if termino in c["nit"].lower() or termino in c["nombre"].lower()
    ]

    if not encontrados:
        mostrar_alerta("No se encontraron clientes.")
        return

    for cliente in encontrados:
        print(f"NIT: {cliente['nit']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print("-" * 40)