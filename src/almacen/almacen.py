'''
Módulo de almacenamiento de datos
'''
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.parent / "data"

def guardar_datos(nombre_archivo: str, datos: any) -> None:
    # Si el archivo no existe, se crea automáticamente
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)

    ruta_archivo = DATA_DIR / nombre_archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

def recuperar_datos(nombre_archivo: str) -> any:
    ruta_archivo = DATA_DIR / nombre_archivo
    if not ruta_archivo.exists():
        return None

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos
