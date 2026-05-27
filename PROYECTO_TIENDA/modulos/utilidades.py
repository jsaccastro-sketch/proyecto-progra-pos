class Colores:
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"
    NEGRITA = "\033[1m"


def mostrar_titulo(texto):
    """Muestra un título con formato."""
    print(f"\n{Colores.AZUL}{Colores.NEGRITA}=== {texto} ==={Colores.RESET}")


def mostrar_exito(mensaje):
    """Muestra mensaje de éxito."""
    print(f"{Colores.VERDE}✅ {mensaje}{Colores.RESET}")


def mostrar_error(mensaje):
    """Muestra mensaje de error."""
    print(f"{Colores.ROJO}❌ {mensaje}{Colores.RESET}")


def mostrar_alerta(mensaje):
    """Muestra mensaje de advertencia."""
    print(f"{Colores.AMARILLO}⚠ {mensaje}{Colores.RESET}")


def pedir_texto(mensaje):
    """Pide texto no vacío al usuario."""
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        mostrar_error("Este campo no puede estar vacío.")


def pedir_entero(mensaje):
    """Pide un número entero positivo."""
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            mostrar_error("El número debe ser mayor que cero.")

        except ValueError:
            mostrar_error("Debe ingresar un número entero válido.")


def pedir_float(mensaje):
    """Pide un número decimal no negativo."""
    while True:
        try:
            numero = float(input(mensaje))

            if numero >= 0:
                return numero

            mostrar_error("El número no puede ser negativo.")

        except ValueError:
            mostrar_error("Debe ingresar un número válido.")


def validar_email(email):
    """Valida un correo electrónico de forma básica."""
    return "@" in email and "." in email


def confirmar_accion(mensaje):
    """Pide confirmación al usuario."""
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"


def login():
    """Solicita usuario y contraseña para entrar al sistema."""
    usuarios = {
        "admin": {
            "password": "1234",
            "rol": "admin"
        },
        "cajero": {
            "password": "1234",
            "rol": "cajero"
        }
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