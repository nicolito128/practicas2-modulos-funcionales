from .libros import Libro
from datetime import datetime
import almacen

def ingresar_full() -> Libro:
    nuevo_libro: Libro = Libro()

    print("========== Ingreso de nuevo Libro ==========")
    nuevo_libro.pedir_isbn()
    nuevo_libro.pedir_titulo()
    nuevo_libro.pedir_autor()
    nuevo_libro.pedir_editorial()
    nuevo_libro.pedir_genero()
    nuevo_libro.pedir_anio()
    nuevo_libro.pedir_ejemplares()

    return nuevo_libro

def dar_baja(libro: Libro) -> bool:
    if not libro.fecha_baja:
        libro.fecha_baja = datetime.today().strftime('%Y-%m-%d')
        return True
    return False

def reactivar_libro(libro: Libro) -> bool:
    if libro.fecha_baja:
        libro.fecha_baja = None
        return True
    return False

def actualizar_ejemplares(libro: Libro, cantidad: int) -> None:
    libro.ejemplares = cantidad
    libro.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')
    return None

def actualizar_libro(libro: Libro) -> None:
    print("=== Actualización de datos del Libro ===")
    loop: bool = True
    while loop:
        print("Seleccione el campo a actualizar:")
        print("1. Título")
        print("2. Autor")
        print("3. Editorial")
        print("4. Género")
        print("5. Año")
        print("6. Cantidad de Ejemplares")
        print("7. Salir")
        opcion: str = input(">> ")

        if opcion == "1":
            libro.pedir_titulo()
        elif opcion == "2":
            libro.pedir_autor()
        elif opcion == "3":
            libro.pedir_editorial()
        elif opcion == "4":
            libro.pedir_genero()
        elif opcion == "5":
            libro.pedir_anio()
        elif opcion == "6":
            libro.pedir_ejemplares()
        elif opcion == "7":
            loop = False
        else:
            print("! Opción no válida. Intente de nuevo.")
    libro.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')

def mostrar_libro(libro: Libro) -> None:
    print("=== Información del Libro ===")
    print(f"ISBN: {libro.isbn}")
    print(f"Título: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"Editorial: {libro.editorial}")
    print(f"Género: {libro.genero}")
    print(f"Año: {libro.anio}")
    print(f"Ejemplares: {libro.ejemplares}")
    print(f"Fecha de Creación: {libro.fecha_creacion}")
    print(f"Fecha de Actualización: {libro.fecha_actualizado}")
    if libro.fecha_baja:
        print(f"Fecha de Baja: {libro.fecha_baja}")
    else:
        print("Estado: Activo")

def guardar_libro(libro: Libro) -> None:
    nombre_libro: str = "libro_{libro.isbn}.json"
    almacen.guardar_datos(nombre_libro, libro.to_dict())

def recuperar_libro_isbn(isbn: str) -> Libro | None:
    nombre_libro: str = f"libro_{isbn}.json"
    datos_libro: dict[str, any] = almacen.recuperar_datos(nombre_libro)
    if datos_libro:
        libro: Libro = Libro()
        libro.isbn = datos_libro["isbn"]
        libro.titulo = datos_libro["titulo"]
        libro.autor = datos_libro["autor"]
        libro.editorial = datos_libro["editorial"]
        libro.genero = datos_libro["genero"]
        libro.anio = datos_libro["anio"]
        libro.ejemplares = datos_libro["ejemplares"]
        libro.fecha_creacion = datos_libro["fecha_creacion"]
        libro.fecha_actualizado = datos_libro["fecha_actualizado"]
        libro.fecha_baja = datos_libro["fecha_baja"]
        return libro
