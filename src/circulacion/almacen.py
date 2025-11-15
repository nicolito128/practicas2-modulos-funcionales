from circulacion import Circulacion

data: [Circulacion] = []

def guardar_circulacion(circ: Circulacion) -> None:
    global data
    for idx, existente in enumerate(data):
        if existente.id_socio == circ.id_socio and existente.isbn_libro == circ.isbn_libro:
            data[idx] = circ
            return
    data.append(circ)

def buscar_circulacion(id_socio: str, isbn_libro: str) -> Circulacion | None:
    global data
    for circ in data:
        if circ.id_socio == id_socio and circ.isbn_libro == isbn_libro:
            return circ
    return None

def listar_circulaciones() -> list[Circulacion]:
    global data
    return data

def eliminar_circulacion(id_socio: int, isbn_libro: str) -> bool:
    global data
    for idx, circ in enumerate(data):
        if circ.id_socio == id and circ.isbn_libro == isbn_libro:
            del data[idx]
            return True
    return False
