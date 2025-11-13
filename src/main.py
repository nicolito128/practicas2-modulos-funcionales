import socios
import libros

# Programa principal que junta al resto de los modulos
def main():
    print("MAIN")

    s = libros.ingresar_full()
    print(s)

# Llama a la función main sólo si es ejecutado como script principal (`python src/main.py`)
if __name__ == "__main__":
    main()
