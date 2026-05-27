from modulos.archivos import cargar_json, guardar_json
from modulos.utilidades import (
    mostrar_titulo,
    mostrar_exito,
    mostrar_error,
    mostrar_alerta,
    pedir_texto,
    validar_email,
    confirmar_accion
)

RUTA_CLIENTES = "datos/clientes.json"
RUTA_VENTAS = "datos/ventas.json"


def cargar_clientes():
    """Carga la lista de clientes desde el archivo JSON."""
    return cargar_json(RUTA_CLIENTES)


def guardar_clientes(clientes):
    """Guarda la lista de clientes en el archivo JSON."""
    guardar_json(RUTA_CLIENTES, clientes)


def buscar_cliente_por_nit(clientes, nit):
    """Busca un cliente por su NIT."""
    for cliente in clientes:
        if cliente["nit"].lower() == nit.lower():
            return cliente

    return None


def cliente_tiene_ventas(nit):
    """Verifica si un cliente tiene ventas registradas."""
    ventas = cargar_json(RUTA_VENTAS)

    for venta in ventas:
        if venta["nit_cliente"].lower() == nit.lower():
            return True

    return False


def registrar_cliente():
    """Registra un nuevo cliente."""
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

    while True:
        email = pedir_texto("Email: ")

        if validar_email(email):
            break

        mostrar_error("Email inválido. Debe contener '@' y '.'.")

    nuevo_cliente = {
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)

    mostrar_exito("Cliente registrado correctamente.")


def listar_clientes():
    """Lista todos los clientes registrados."""
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

    encontrados = []

    for cliente in clientes:
        if termino in cliente["nit"].lower() or termino in cliente["nombre"].lower():
            encontrados.append(cliente)

    if not encontrados:
        mostrar_alerta("No se encontraron clientes.")
        return

    for cliente in encontrados:
        print(f"NIT: {cliente['nit']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print("-" * 40)


def actualizar_cliente():
    """Actualiza teléfono o email de un cliente."""
    mostrar_titulo("ACTUALIZAR CLIENTE")

    clientes = cargar_clientes()
    nit = pedir_texto("Ingrese NIT del cliente: ")

    cliente = buscar_cliente_por_nit(clientes, nit)

    if not cliente:
        mostrar_error("Cliente no encontrado.")
        return

    print("1. Actualizar teléfono")
    print("2. Actualizar email")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        cliente["telefono"] = pedir_texto("Nuevo teléfono: ")

    elif opcion == "2":
        while True:
            nuevo_email = pedir_texto("Nuevo email: ")

            if validar_email(nuevo_email):
                cliente["email"] = nuevo_email
                break

            mostrar_error("Email inválido.")

    else:
        mostrar_error("Opción inválida.")
        return

    guardar_clientes(clientes)

    mostrar_exito("Cliente actualizado correctamente.")


def eliminar_cliente():
    """Elimina un cliente si no tiene ventas registradas."""
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


def menu_clientes():
    """Muestra el menú del módulo de clientes."""
    while True:
        mostrar_titulo("MÓDULO DE CLIENTES")

        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("0. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "0":
            break
        else:
            mostrar_error("Opción inválida.")