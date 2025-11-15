import socios
import libros
import circulacion

def menu_principal() -> None:
    print("=== Menú Principal ===")
    print("1. Gestión de Socios")
    print("2. Gestión de Libros")
    print("3. Gestión de Circulación")
    print("4. Salir")

    opcion: str = input(">> ")

    if opcion == "1":
        socios.menu_socios()
    elif opcion == "2":
        libros.menu_libros()
    elif opcion == "3":
        circulacion.menu_circulacion()
    elif opcion == "4":
        print("Saliendo del programa...")
        return
    else:
        print("Opción no válida. Intente de nuevo.")
    menu_principal()
