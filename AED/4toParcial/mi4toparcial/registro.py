import random

class Vehiculo:
    def __init__(self, id, tamaño, tipo, costo):
        self.id = id
        self.tamaño = tamaño
        self.tipo = tipo
        self.costo = costo

def to_string(vehiculo):
    r = ' '
    r += '| Id: {:<10}'.format(vehiculo.id)
    r += '| Tamaño: {:<30}'.format(vehiculo.tamaño)
    r += '| Tipo: {:<30}'.format(vehiculo.tipo)
    r += '| Costo:$ {:<20}'.format(vehiculo.costo) + '|'
    return r

def generador(vec, n):
    for i in range(n):
        id = random.randint(1000, 9999)
        tamaño = random.randint(1, 4)
        tipo =  random.randint(0, 4)
        costo = random.randint(10000, 99999)
        nuevoVehiculo = Vehiculo(id, tamaño, tipo, costo)
        add_in_order(vec, nuevoVehiculo)

def add_in_order(vec, reg):
    izq, der = 0, len(vec) - 1
    pos = 0
    while izq <= der:
        centro = (izq + der) // 2
        if vec[centro].id == reg.id:
            pos = centro
            break
        if reg.id < vec[centro].id:
            der = centro - 1
        else:
            izq = centro + 1
        if izq > der:
            pos = izq
    vec[pos:pos] = [reg]











