from libros import Libro

data: [Libro] = []

def guardar_libro(libro: Libro) -> None:
    global data
    # Verificar si el libro ya existe (por ISBN)
    for idx, existente in enumerate(data):
        if existente.isbn == libro.isbn:
            data[idx] = libro
            return
    data.append(libro)

def buscar_libro(isbn: str) -> Libro | None:
    global data
    for libro in data:
        if libro.isbn == isbn:
            return libro
    return None

def listar_libros() -> list[Libro]:
    global data
    return data

def eliminar_libro(isbn: str) -> bool:
    global data
    for idx, libro in enumerate(data):
        if libro.isbn == isbn:
            del data[idx]
            return True
    return False
