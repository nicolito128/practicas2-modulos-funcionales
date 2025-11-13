'''
Módulo de gestión de socios
'''
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Socio:
    dni: int
    nombre: str
    apellido: str
    genero: str
    email: str
    direccion: str
    telefono: str
    categoria: str
    fecha_creacion: datetime
    fecha_actualizado: datetime
    fecha_baja: datetime | None

    def __init__(self):
        self.dni = 0
        self.nombre = ""
        self.apellido = ""
        self.genero = ""
        self.email = ""
        self.direccion = ""
        self.telefono = ""
        self.categoria = ""
        self.fecha_creacion = datetime.today().strftime('%Y-%m-%d')
        self.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')
        self.fecha_baja = None

    def pedir_dni(self) -> None:
        dni_in: int
        repeat: bool = True
        while repeat:
            try:
                dni_in = int(input("> Ingrese un DNI: "))
                repeat = False
            except Exception:
                print("! No se pudo convertir el valor ingresado a un número.")
                print("! Intente de nuevo.")
        self.dni = dni_in

    def pedir_nombre(self) -> None:
        nombre_in: str
        repeat: bool = True
        while repeat:
            try:
                nombre_in = input("> Ingrese un Nombre: ")
                if len(nombre_in) > 0 and nombre_in.isalpha():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un nombre válido.")
                print("! Intente de nuevo.")
        self.nombre = nombre_in

    def pedir_apellido(self) -> None:
        apellido_in: str
        repeat: bool = True
        while repeat:
            try:
                apellido_in = input("> Ingrese un Apellido: ")
                if len(apellido_in) > 0 and apellido_in.isalpha():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un apellido válido.")
                print("! Intente de nuevo.")
        self.apellido = apellido_in

    def pedir_genero(self) -> None:
        generos = {'M': 'Masculino', 'F': 'Femenino', 'O': 'Otro', 'N': 'No especificar'}
        genero_in: str
        repeat: bool = True
        while repeat:
            try:
                print("> Ingrese un Género:")
                for key, value in generos.items():
                    print(f"  {key}: {value}")
                genero_in = input(">> ").upper()
                if genero_in in generos.keys():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un género válido.")
                print("! Intente de nuevo.")

    def pedir_email(self) -> None:
        email_in: str
        repeat: bool = True
        while repeat:
            try:
                email_in = input("> Ingrese un Email: ")
                if "@" in email_in and "." in email_in:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un email válido.")
                print("! Intente de nuevo.")
        self.email = email_in

    def pedir_direccion(self) -> None:
        dir_in: str
        repeat: bool = True
        while repeat:
            try:
                dir_in = input("> Ingrese una Dirección: ")
                if len(dir_in) > 0:
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó una dirección válida.")
                print("! Intente de nuevo.")
        self.direccion = dir_in

    def pedir_telefono(self) -> None:
        tel_in: str
        repeat: bool = True
        while repeat:
            try:
                tel_in = input("> Ingrese un Teléfono: ")
                if len(tel_in) > 0 and tel_in.isdigit():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó un teléfono válido.")
                print("! Intente de nuevo.")

    def pedir_categoria(self) -> None:
        categorias = {'A': 'Activo', 'I': 'Inactivo', 'S': 'Suspendido'}
        categoria_in: str
        repeat: bool = True
        while repeat:
            try:
                print("> Ingrese una Categoría:")
                for key, value in categorias.items():
                    print(f"  {key}: {value}")
                categoria_in = input(">> ").upper()
                if categoria_in in categorias.keys():
                    repeat = False
                else:
                    raise Exception
            except Exception:
                print("! No se ingresó una categoría válida.")
                print("! Intente de nuevo.")
        self.categoria = categoria_in

def ingresar_full() -> Socio:
    nuevo_socio: Socio = Socio()

    print("========== Ingreso de nuevo Socio ==========")
    nuevo_socio.pedir_dni()
    nuevo_socio.pedir_nombre()
    nuevo_socio.pedir_apellido()
    nuevo_socio.pedir_genero()
    nuevo_socio.pedir_email()
    nuevo_socio.pedir_direccion()
    nuevo_socio.pedir_telefono()
    nuevo_socio.pedir_categoria()

    return nuevo_socio

__all__ = ["Socio", "ingresar_full"]
