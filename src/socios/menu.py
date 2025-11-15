import socios
import socios.almacen as almacen
from socios import Socio

def menu_socios() -> None:
    loop: bool = True
    while loop:
        print("\n=== Menú de Gestión de Socios ===")
        print("1. Ingresar nuevo Socio")
        print("2. Dar de baja un Socio")
        print("3. Reactivar un Socio")
        print("4. Actualizar datos de un Socio")
        print("5. Mostrar datos de un Socio")
        print("6. Volver al Menú Principal")

        opcion: str = input(">> ")

        if opcion == "1":
            nuevo_socio: Socio = socios.ingresar_full()
            try:
                almacen.guardar_socio(nuevo_socio)
                print("\n+ Socio ingresado exitosamente. +")
            except Exception as e:
                print(f"\n! Error al guardar el socio: {e}")

        elif opcion == "2":
            print("\n--- Dar de baja un Socio ---")
            try:
                dni_buscar = int(input("> Ingrese el DNI del socio a dar de baja: "))
                # Se asume que almacen.buscar_socio(dni) devuelve un objeto Socio o None
                socio_encontrado = almacen.buscar_socio(dni_buscar)

                if socio_encontrado:
                    if socios.dar_baja(socio_encontrado):
                        almacen.guardar_socio(socio_encontrado)
                        print(f"\n+ Socio DNI {dni_buscar} dado de baja exitosamente. +")
                    else:
                        print(f"\n! El socio DNI {dni_buscar} ya se encontraba dado de baja.")
                else:
                    print(f"\n! No se encontró ningún socio con el DNI: {dni_buscar}")
            except ValueError:
                print("\n! DNI no válido. Debe ser un número.")
            except Exception as e:
                print(f"\n! Error al buscar o guardar socio: {e}")
                print("! (Asegúrese que 'almacen.buscar_socio' esté implementado)")

        elif opcion == "3":
            print("\n--- Reactivar un Socio ---")
            try:
                dni_buscar = int(input("> Ingrese el DNI del socio a reactivar: "))
                socio_encontrado = almacen.buscar_socio(dni_buscar)

                if socio_encontrado:
                    if socios.reactivar_socio(socio_encontrado):
                        almacen.guardar_socio(socio_encontrado)
                        print(f"\n+ Socio DNI {dni_buscar} reactivado exitosamente. +")
                    else:
                        print(f"\n! El socio DNI {dni_buscar} ya se encontraba activo.")
                else:
                    print(f"\n! No se encontró ningún socio con el DNI: {dni_buscar}")
            except ValueError:
                print("\n! DNI no válido. Debe ser un número.")
            except Exception as e:
                print(f"\n! Error al buscar o guardar socio: {e}")
                print("! (Asegúrese que 'almacen.buscar_socio' esté implementado)")

        elif opcion == "4":
            print("\n--- Actualizar datos de un Socio ---")
            try:
                dni_buscar = int(input("> Ingrese el DNI del socio a actualizar: "))
                socio_encontrado = almacen.buscar_socio(dni_buscar)
                print(socio_encontrado)

                if socio_encontrado:
                    socios.actualizar_socio(socio_encontrado)
                    almacen.guardar_socio(socio_encontrado)
                    print(f"\n+ Socio DNI {dni_buscar} actualizado exitosamente. +")
                else:
                    print(f"\n! No se encontró ningún socio con el DNI: {dni_buscar}")
            except ValueError:
                print("\n! DNI no válido. Debe ser un número.")
            except Exception as e:
                print(f"\n! Error al buscar o guardar socio: {e}")
                print("! (Asegúrese que 'almacen.buscar_socio' esté implementado)")

        elif opcion == "5":
            print("\n--- Mostrar datos de un Socio ---")
            try:
                dni_buscar = int(input("> Ingrese el DNI del socio a mostrar: "))
                socio_encontrado = almacen.buscar_socio(dni_buscar)

                if socio_encontrado:
                    socios.mostrar_socio(socio_encontrado)
                else:
                    print(f"\n! No se encontró ningún socio con el DNI: {dni_buscar}")
            except ValueError:
                print("\n! DNI no válido. Debe ser un número.")
            except Exception as e:
                print(f"\n! Error al buscar socio: {e}")
                print("! (Asegúrese que 'almacen.buscar_socio' esté implementado)")

        elif opcion == "6":
            print("\nVolviendo al Menú Principal...")
            loop = False

        else:
            print("\n! Opción no válida. Intente de nuevo.")
            # El bucle while se encargará de volver a mostrar el menú
