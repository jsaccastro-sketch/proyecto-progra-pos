# clientes_crud.py
# CRUD de clientes

from modulos.archivos import cargar_json
from modulos.utilidades import (
    mostrar_titulo, mostrar_exito, mostrar_error, mostrar_alerta,
    pedir_texto, validar_email, confirmar_accion
)
from modulos.clientes_busqueda import (
    cargar_clientes, guardar_clientes, buscar_cliente_por_nit
)

RUTA_VENTAS = "datos/ventas.json"


def cliente_tiene_ventas(nit):
    """Verifica si un cliente tiene ventas."""
    ventas = cargar_json(RUTA_VENTAS)

    for venta in ventas:
        if venta["nit_cliente"].lower() == nit.lower():
            return True

    return False


def registrar_cliente():
    """Registra un cliente nuevo."""
    mostrar_titulo("REGISTRAR CLIENTE")
    clientes = cargar_clientes()
    nit = pedir_texto("NIT: ")

    if nit.upper() == "CF":
        mostrar_error("No se puede registrar el NIT CF.")
        return

    if buscar_cliente_por_nit(clientes, nit):
        mostrar_error("Ya existe un cliente con ese NIT.")
        return

    nombre = pedir_texto("Nombre: ")
    telefono = pedir_texto("Teléfono: ")
    email = pedir_email()

    clientes.append({
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    })

    guardar_clientes(clientes)
    mostrar_exito("Cliente registrado correctamente.")


def pedir_email():
    """Pide un email válido."""
    while True:
        email = pedir_texto("Email: ")

        if validar_email(email):
            return email

        mostrar_error("Email inválido. Debe contener '@' y '.'.")


def actualizar_cliente():
    """Actualiza teléfono o email."""
    mostrar_titulo("ACTUALIZAR CLIENTE")
    clientes = cargar_clientes()
    nit = pedir_texto("Ingrese NIT del cliente: ")
    cliente = buscar_cliente_por_nit(clientes, nit)

    if not cliente:
        mostrar_error("Cliente no encontrado.")
        return

    cambiar_dato_cliente(cliente)
    guardar_clientes(clientes)
    mostrar_exito("Cliente actualizado correctamente.")


def cambiar_dato_cliente(cliente):
    """Cambia teléfono o email del cliente."""
    print("1. Actualizar teléfono")
    print("2. Actualizar email")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        cliente["telefono"] = pedir_texto("Nuevo teléfono: ")
    elif opcion == "2":
        cliente["email"] = pedir_email()
    else:
        mostrar_error("Opción inválida.")


def eliminar_cliente():
    """Elimina un cliente si no tiene ventas."""
    mostrar_titulo("ELIMINAR CLIENTE")
    clientes = cargar_clientes()
    nit = pedir_texto("Ingrese NIT del cliente: ")
    cliente = buscar_cliente_por_nit(clientes, nit)

    if not cliente:
        mostrar_error("Cliente no encontrado.")
        return

    if cliente_tiene_ventas(nit):
        mostrar_error("No se puede eliminar un cliente con ventas registradas.")
        return

    if confirmar_accion(f"¿Eliminar a {cliente['nombre']}?"):
        clientes.remove(cliente)
        guardar_clientes(clientes)
        mostrar_exito("Cliente eliminado correctamente.")
    else:
        mostrar_alerta("Operación cancelada.")