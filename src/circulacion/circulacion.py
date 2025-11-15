'''
Módulo de gestión de circulaciones: prestamos y devoluciones
'''
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Circulacion:
    id_socio: int
    isbn_libro: str
    fecha_prestamo: str
    fecha_devolucion: str | None

    def __init__(self):
        self.id_socio = ""
        self.isbn_libro = ""
        self.fecha_prestamo = datetime.today().strftime('%Y-%m-%d')
        self.fecha_devolucion = None

    def registrar_devolucion(self) -> None:
        self.fecha_devolucion = datetime.today().strftime('%Y-%m-%d')

    def to_dict(self) -> dict:
        return {
            "id_socio": self.id_socio,
            "isbn_libro": self.isbn_libro,
            "fecha_prestamo": self.fecha_prestamo,
            "fecha_devolucion": self.fecha_devolucion
        }

def registrar_prestamo(id_socio: int, isbn_libro: str) -> Circulacion:
    nuevo_prestamo: Circulacion = Circulacion()
    nuevo_prestamo.id_socio = id_socio
    nuevo_prestamo.isbn_libro = isbn_libro
    return nuevo_prestamo

def registrar_devolucion(c: Circulacion) -> None:
    c.registrar_devolucion()

def actualizar_circulacion(c: Circulacion) -> None:
    print("=== Actualización de datos de la Circulación ===")
    loop: bool = True
    while loop:
        print("Seleccione el campo a actualizar:")
        print("1. Fecha de Préstamo")
        print("2. Fecha de Devolución")
        print("3. Salir")
        opcion: str = input(">> ")

        if opcion == "1":
            fecha_in: str
            repeat: bool = True
            while repeat:
                try:
                    fecha_in = input("> Ingrese la nueva Fecha de Préstamo (YYYY-MM-DD): ")
                    datetime.strptime(fecha_in, '%Y-%m-%d')
                    repeat = False
                except Exception:
                    print("! No se ingresó una fecha válida.")
                    print("! Intente de nuevo.")
            c.fecha_prestamo = fecha_in
        elif opcion == "2":
            fecha_in: str
            repeat: bool = True
            while repeat:
                try:
                    fecha_in = input("> Ingrese la nueva Fecha de Devolución (YYYY-MM-DD): ")
                    datetime.strptime(fecha_in, '%Y-%m-%d')
                    repeat = False
                except Exception:
                    print("! No se ingresó una fecha válida.")
                    print("! Intente de nuevo.")
            c.fecha_devolucion = fecha_in
        elif opcion == "3":
            loop = False

# Implementar el menú de circulacion
def menu_circulacion() -> None:
    print("=== Menú de Circulación ===")
