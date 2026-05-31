# utilidades.py
# Utilidades generales del sistema

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
    """Muestra un mensaje de éxito."""
    print(f"{Colores.VERDE}✅ {mensaje}{Colores.RESET}")


def mostrar_error(mensaje):
    """Muestra un mensaje de error."""
    print(f"{Colores.ROJO}❌ {mensaje}{Colores.RESET}")


def mostrar_alerta(mensaje):
    """Muestra una advertencia."""
    print(f"{Colores.AMARILLO}⚠ {mensaje}{Colores.RESET}")


def pedir_texto(mensaje):
    """Pide texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        mostrar_error("Este campo no puede estar vacío.")


def pedir_entero(mensaje):
    """Pide un entero positivo."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            mostrar_error("El número debe ser mayor que cero.")
        except ValueError:
            mostrar_error("Debe ingresar un número entero válido.")


def validar_email(email):
    """Valida un email básico."""
    return "@" in email and "." in email


def confirmar_accion(mensaje):
    """Confirma una acción con s/n."""
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"