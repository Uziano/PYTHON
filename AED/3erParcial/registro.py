class Figurita:
    def __init__(self, pais, numero, nombre, posicion, valor):
        self.pais = pais
        self.numero = numero
        self.nombre = nombre
        self.posicion = posicion
        self.valor = valor

def to_string(figurita):
    r = ''
    r += '|Pais: {:<5}'.format(figurita.pais)
    r += '|Numero: {:<5}'.format(figurita.numero)
    r += '|Nombre: {:<20}'.format(figurita.nombre)
    r += '|Posicion: {:<5}'.format(figurita.posicion)
    r += '|Valor: {:<10}'.format(figurita.valor)
    return r

def to_string2(figurita):
    print('Pais:', figurita.pais, end=' | ')
    print('Numero:', figurita.numero, end=' | ')
    print('Nombre:', figurita.nombre, end=' | ')
    print('Posicion:', figurita.posicion, end=' | ')
    print('Valor:', figurita.valor)












