# clientes.py
# Menú del módulo de clientes

from modulos.utilidades import mostrar_titulo, mostrar_error
from modulos.clientes_crud import registrar_cliente, actualizar_cliente, eliminar_cliente
from modulos.clientes_busqueda import listar_clientes, buscar_cliente


def menu_clientes():
    """Muestra el menú de clientes."""
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