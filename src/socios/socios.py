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

    def to_dict(self) -> dict[str, any]:
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "genero": self.genero,
            "email": self.email,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "categoria": self.categoria,
            "fecha_creacion": self.fecha_creacion,
            "fecha_actualizado": self.fecha_actualizado,
            "fecha_baja": self.fecha_baja
        }

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

def dar_baja(s: Socio) -> bool:
    if not s.fecha_baja:
        s.fecha_baja = datetime.today().strftime('%Y-%m-%d')
        return True
    else:
        return False

def reactivar_socio(s: Socio) -> bool:
    if s.fecha_baja:
        s.fecha_baja = None
        return True
    else:
        return False

def actualizar_socio(s: Socio) -> None:
    print("\n========== Actualización de datos del Socio ==========")
    loop: bool = True
    cambios_realizados: bool = False

    while loop:
        print("Seleccione el campo a actualizar:")
        print("  1: Nombre")
        print("  2: Apellido")
        print("  3: Género")
        print("  4: Email")
        print("  5: Dirección")
        print("  6: Teléfono")
        print("  7: Categoría")
        print("  0: Finalizar actualización")
        opcion: str = input(">> ")

        if opcion == '1':
            s.pedir_nombre()
            cambios_realizados = True
        elif opcion == '2':
            s.pedir_apellido()
            cambios_realizados = True
        elif opcion == '3':
            s.pedir_genero()
            cambios_realizados = True
        elif opcion == '4':
            s.pedir_email()
            cambios_realizados = True
        elif opcion == '5':
            s.pedir_direccion()
            cambios_realizados = True
        elif opcion == '6':
            s.pedir_telefono()
            cambios_realizados = True
        elif opcion == '7':
            s.pedir_categoria()
            cambios_realizados = True
        elif opcion == '0':
            loop = False
        else:
            print("! Opción no válida. Intente de nuevo.")

    if cambios_realizados:
        s.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')
        print("+ Datos actualizados correctamente.")
    else:
        print("\n> No se realizó ninguna modificación.")

def mostrar_socio(s: Socio) -> None:
    print("========== Datos del Socio ==========")
    print(f"- DNI: {s.dni}")
    print(f"- Nombre: {s.nombre}")
    print(f"- Apellido: {s.apellido}")
    print(f"- Género: {s.genero}")
    print(f"- Email: {s.email}")
    print(f"- Dirección: {s.direccion}")
    print(f"- Teléfono: {s.telefono}")
    print(f"- Categoría: {s.categoria}")
    print(f"- Fecha de Creación: {s.fecha_creacion}")
    print(f"- Fecha de Actualización: {s.fecha_actualizado}")
    print(f"- Fecha de Baja: {s.fecha_baja if s.fecha_baja else 'Activo'}")
