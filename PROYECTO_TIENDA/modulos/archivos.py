import json
import os


def cargar_json(ruta):
    try:
        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except json.JSONDecodeError:
        return []


def guardar_json(ruta, datos):
    carpeta = os.path.dirname(ruta)

    if carpeta:
        os.makedirs(carpeta, exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)