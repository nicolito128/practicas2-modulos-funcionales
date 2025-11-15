from socios import Socio

data: [Socio] = []

def guardar_socio(socio: Socio) -> None:
    global data
    # Verificar si el socio ya existe (por DNI)
    for idx, existente in enumerate(data):
        if existente.dni == socio.dni:
            data[idx] = socio
            return
    data.append(socio)

def buscar_socio(dni: int) -> Socio | None:
    global data
    for socio in data:
        if socio.dni == dni:
            return socio
    return None

def listar_socios() -> list[Socio]:
    global data
    return data

def eliminar_socio(dni: int) -> bool:
    global data
    for idx, socio in enumerate(data):
        if socio.dni == dni:
            del data[idx]
            return True
    return False
