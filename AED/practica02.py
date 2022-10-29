import pickle 
import os.path
import os

class Coffee():
    def __init__(self, Nombre, Sabor, Crema, Lugar):
        self.nombre = Nombre
        self.sabor = Sabor
        self.lugar = Lugar
        self.crema = False
        

def display(cafe):
    print('|Nombre:', cafe.nombre, end='|')
    print('Sabor:', cafe.sabor, end='|')
    print('Lugar:', cafe.lugar, end='|')


def test():
    cof1 = Coffee('Espresso', 'Fuerte', 'serendipia', False)
    display(cof1)
if __name__ == '__main__':
    test()








