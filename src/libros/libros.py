'''
Módulo de gestión de libros
'''
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Libro:
    isbn: str
    titulo: str
    autor: str
    editorial: str
    genero: str
    anio: int
    ejemplares: int
    fecha_creacion: datetime
    fecha_actualizado: datetime
    fecha_baja: datetime | None

    def __init__(self):
        self.isbn = ""
        self.titulo = ""
        self.autor = ""
        self.editorial = ""
        self.genero = ""
        self.anio = 0
        self.ejemplares = 0
        self.fecha_creacion = datetime.today().strftime('%Y-%m-%d')
        self.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')
        self.fecha_baja = None

    def pedir_isbn(self) -> None:
        isbn_in: str
        repeat: bool = True
        while repeat:
            try:
                isbn_in = input("> Ingrese ISBN: ")
                if len(isbn_in) > 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un ISBN válido.")
                print("! Intente de nuevo.")
        self.isbn = isbn_in

    def pedir_titulo(self) -> None:
        titulo_in: str
        repeat: bool = True
        while repeat:
            try:
                titulo_in = input("> Ingrese el Título: ")
                if len(titulo_in) > 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un título válido.")
                print("! Intente de nuevo.")
        self.titulo = titulo_in

    def pedir_autor(self) -> None:
        autor_in: str
        repeat: bool = True
        while repeat:
            try:
                autor_in = input("> Ingrese el Autor: ")
                if len(autor_in) > 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un autor válido.")
                print("! Intente de nuevo.")
        self.autor = autor_in

    def pedir_editorial(self) -> None:
        edi_in: str
        repeat: bool = True
        while repeat:
            try:
                edi_in = input("> Ingrese la Editorial: ")
                if len(edi_in) > 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó una editorial válida.")
                print("! Intente de nuevo.")
        self.editorial = edi_in

    def pedir_genero(self) -> None:
        genero_in: str
        repeat: bool = True
        while repeat:
            try:
                genero_in = input("> Ingrese el Género: ")
                if len(genero_in) > 0 and genero_in.isalpha():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un género válido (sólo letras).")
                print("! Intente de nuevo.")
        self.genero = genero_in

    def pedir_anio(self) -> None:
        anio_in: int
        repeat: bool = True
        current_year = datetime.today().year
        while repeat:
            try:
                anio_in = int(input("> Ingrese el Año de publicación (ej.: 2025): "))
                if 1000 <= anio_in <= current_year:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un año válido.")
                print("! Intente de nuevo.")
        self.anio = anio_in

    def pedir_ejemplares(self) -> None:
        ej_in: int
        repeat: bool = True
        while repeat:
            try:
                ej_in = int(input("> Ingrese la cantidad de ejemplares: "))
                if ej_in >= 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó una cantidad válida de ejemplares.")
                print("! Intente de nuevo.")
        self.ejemplares = ej_in

    def to_dict(self) -> dict[str, any]:
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "editorial": self.editorial,
            "genero": self.genero,
            "anio": self.anio,
            "ejemplares": self.ejemplares,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizado": self.fecha_actualizado,
            "fecha_baja": self.fecha_baja,
        }

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
