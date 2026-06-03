"""
Módulo: archivos.py
Descripción: Para guardar y abrir los archivos JSON del sistema.
Autor: Josue Saul Sac Castro
Fecha: Mayo 2026
"""

import json
import os


def cargar_json(ruta):
    """
    Abre un archivo JSON y devuelve los datos en una lista.
    Si el archivo no existe o está roto, devuelve una lista vacía para que no truene.
    """
    try:
        # Si el archivo no existe en la compu, avisa mandando una lista vacía
        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        # Si da cualquier error raro, manda lista vacía para estar seguros
        return []


def guardar_json(ruta, datos):
    """
    Saca los datos del programa y los guarda en el archivo JSON.
    Si la carpeta no existe, la crea de una vez.
    """
    try:
        carpeta = os.path.dirname(ruta)

        # Crea la carpeta (como datos/) si todavía no existe
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True

    except (TypeError, OSError, PermissionError):
        # Si pasa algo malo al guardar, avisa con un False
        return False