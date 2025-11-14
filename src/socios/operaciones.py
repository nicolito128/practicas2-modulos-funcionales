from .socios import Socio
from datetime import datetime
import almacen

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
    print("========== Actualización de datos del Socio ==========")
    loop: bool = True
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
        elif opcion == '2':
            s.pedir_apellido()
        elif opcion == '3':
            s.pedir_genero()
        elif opcion == '4':
            s.pedir_email()
        elif opcion == '5':
            s.pedir_direccion()
        elif opcion == '6':
            s.pedir_telefono()
        elif opcion == '7':
            s.pedir_categoria()
        elif opcion == '0':
            loop = False
        else:
            print("! Opción no válida. Intente de nuevo.")
    s.fecha_actualizado = datetime.today().strftime('%Y-%m-%d')

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

def guardar_socio(s: Socio) -> None:
    nombre_archivo: str = f"socio_{s.dni}.json"
    almacen.guardar_datos(nombre_archivo, s.to_dict())
    print(f"> Socio guardado en el archivo '{nombre_archivo}'.")

def recuperar_socio_dni(dni: int) -> Socio | None:
    nombre_archivo: str = f"socio_{dni}.json"
    datos = almacen.recuperar_datos(nombre_archivo)
    if datos:
        socio_recuperado = Socio()
        socio_recuperado.dni = datos["dni"]
        socio_recuperado.nombre = datos["nombre"]
        socio_recuperado.apellido = datos["apellido"]
        socio_recuperado.genero = datos["genero"]
        socio_recuperado.email = datos["email"]
        socio_recuperado.direccion = datos["direccion"]
        socio_recuperado.telefono = datos["telefono"]
        socio_recuperado.categoria = datos["categoria"]
        socio_recuperado.fecha_creacion = datos["fecha_creacion"]
        socio_recuperado.fecha_actualizado = datos["fecha_actualizado"]
        socio_recuperado.fecha_baja = datos["fecha_baja"]
        return socio_recuperado
