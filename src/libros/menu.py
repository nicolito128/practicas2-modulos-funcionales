from libros import Libro
import libros
import libros.almacen as almacen

def menu_libros() -> None:
    loop: bool = True
    while loop:
        print("\n=== Menú de Gestión de Libros ===")
        print("1. Ingresar nuevo Libro")
        print("2. Buscar un Libro por ISBN")
        print("3. Listar todos los Libros")
        print("4. Eliminar un Libro por ISBN")
        print("5. Volver al Menú Principal")

        opcion: str = input(">> ")

        if opcion == "1":
            nuevo_libro: Libro = libros.ingresar_full()
            try:
                almacen.guardar_libro(nuevo_libro)
                print("\n+ Libro ingresado exitosamente. +")
            except Exception as e:
                print(f"\n! Error al guardar el libro: {e}")

        elif opcion == "2":
            isbn_buscar = input("> Ingrese el ISBN del libro a buscar: ")
            try:
                libro_encontrado = almacen.buscar_libro(isbn_buscar)
                if libro_encontrado:
                    libros.mostrar_libro(libro_encontrado)
                else:
                    print(f"\n! No se encontró ningún libro con el ISBN: {isbn_buscar}")
            except Exception as e:
                print(f"\n! Error al buscar el libro: {e}")

        elif opcion == "3":
            print("\n--- Listado de Libros ---")
            try:
                lista_libros = almacen.listar_libros()
                for libro in lista_libros:
                    libros.mostrar_libro(libro)
            except Exception as e:
                print(f"\n! Error al listar los libros: {e}")

        elif opcion == "4":
            isbn_eliminar = input("> Ingrese el ISBN del libro a eliminar: ")
            try:
                if almacen.eliminar_libro(isbn_eliminar):
                    print(f"\n+ Libro con ISBN {isbn_eliminar} eliminado exitosamente. +")
                else:
                    print(f"\n! No se encontró ningún libro con el ISBN: {isbn_eliminar}")
            except Exception as e:
                print(f"\n! Error al eliminar el libro: {e}")

        elif opcion == "5":
            print("\nVolviendo al Menú Principal...")
            loop = False

        else:
            print("\n! Opción no válida. Intente de nuevo.")
            # El bucle while se encargará de volver a mostrar el menú
