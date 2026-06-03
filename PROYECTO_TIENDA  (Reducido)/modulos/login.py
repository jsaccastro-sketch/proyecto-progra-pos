from modulos.utilidades import mostrar_titulo, mostrar_exito, mostrar_error


def login():
    """Solicita usuario y contraseña."""
    usuarios = {
        "admin": {"password": "1234", "rol": "admin"},
        "cajero": {"password": "1234", "rol": "cajero"}
    }

    mostrar_titulo("LOGIN DEL SISTEMA")

    for intento in range(3):
        usuario = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if usuario in usuarios and usuarios[usuario]["password"] == password:
            mostrar_exito(f"Bienvenido, {usuario}")
            return usuarios[usuario]["rol"]

        mostrar_error("Usuario o contraseña incorrectos.")

    mostrar_error("Demasiados intentos fallidos.")
    return None