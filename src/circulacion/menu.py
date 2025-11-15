from circulacion import Circulacion
import circulacion
import circulacion.almacen as almacen
import libros.almacen as almacen_libros
import socios.almacen as almacen_socios

def menu_circulacion() -> None:
    print("=== Menú de Circulación ===")
    loop: bool = True
    while loop:
        print("1. Registrar Préstamo")
        print("2. Registrar Devolución")
        print("3. Actualizar datos de Circulación")
        print("4. Volver al Menú Principal")

        opcion: str = input(">> ")

        if opcion == "1":
            try:

                id_socio = int(input("> Ingrese el DNI del socio: "))
                if almacen_socios.buscar_socio(id_socio) is None:
                    print(f"\n! No se encontró ningún socio con DNI {id_socio}")
                    continue

                isbn_libro = input("> Ingrese el ISBN del libro: ")
                if almacen_libros.buscar_libro(isbn_libro) is None:
                    print(f"\n! No se encontró ningún libro con ISBN {isbn_libro}")
                    continue

                # Verificar si el socio y el libro existen antes de registrar el préstamo
                if not almacen.buscar_circulacion(id_socio, isbn_libro) is None:
                    print(f"\n! Ya existe un préstamo activo para el socio ID {id_socio} y libro ISBN {isbn_libro}")
                    continue

                nuevo_prestamo: Circulacion = circulacion.registrar_prestamo(id_socio, isbn_libro)
                almacen.guardar_circulacion(nuevo_prestamo)
                print("\n+ Préstamo registrado exitosamente. +")
            except Exception as e:
                print(f"\n! Error al guardar el préstamo: {e}")

        elif opcion == "2":
            try:
                id_socio = int(input("> Ingrese el DNI del socio: "))
                if almacen_socios.buscar_socio(id_socio) is None:
                    print(f"\n! No se encontró ningún socio con DNI {id_socio}")
                    continue

                isbn_libro = input("> Ingrese el ISBN del libro: ")
                if almacen_libros.buscar_libro(isbn_libro) is None:
                    print(f"\n! No se encontró ningún libro con ISBN {isbn_libro}")
                    continue

                circulacion_encontrada = almacen.buscar_circulacion(id_socio, isbn_libro)
                if circulacion_encontrada:
                    circulacion.registrar_devolucion(circulacion_encontrada)
                    almacen.guardar_circulacion(circulacion_encontrada)
                    print("\n+ Devolución registrada exitosamente. +")
                else:
                    print(f"\n! No se encontró ninguna circulación para el socio ID {id_socio} y libro ISBN {isbn_libro}")
            except Exception as e:
                print(f"\n! Error al registrar la devolución: {e}")

        elif opcion == "3":
            try:
                id_socio = int(input("> Ingrese el DNI del socio: "))
                if almacen_socios.buscar_socio(id_socio) is None:
                    print(f"\n! No se encontró ningún socio con DNI {id_socio}")
                    continue

                isbn_libro = input("> Ingrese el ISBN del libro: ")
                if almacen_libros.buscar_libro(isbn_libro) is None:
                    print(f"\n! No se encontró ningún libro con ISBN {isbn_libro}")
                    continue

                circulacion_encontrada = almacen.buscar_circulacion(id_socio, isbn_libro)
                if circulacion_encontrada:
                    circulacion.actualizar_circulacion(circulacion_encontrada)
                    almacen.guardar_circulacion(circulacion_encontrada)
                    print("\n+ Circulación actualizada exitosamente. +")
                else:
                    print(f"\n! No se encontró ninguna circulación para el socio ID {id_socio} y libro ISBN {isbn_libro}")
            except Exception as e:
                print(f"\n! Error al actualizar la circulación: {e}")
        elif opcion == "4":
            print("\nVolviendo al Menú Principal...")
            loop = False
        else:
            print("\n! Opción no válida. Intente de nuevo.")
            # El bucle while se encargará de volver a mostrar el menú
