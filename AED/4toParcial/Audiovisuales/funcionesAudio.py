import pickle
import random
import os.path
from registro import *

vec = []

def menu():
    print('\n| Menu de Opciones |')
    print('1 - Cargar Datos en Orden')
    print('2 - Mostrar con repos mayor a c')
    print('3 - Matriz')
    print('4 - Generar Archivo con contenido !4 8 y 12 y repos may a c')
    print('5 - Mostrar Archivo')
    print('0 - Salir')

def generador(vector, n):
    lista_nombres = 'Youtube', 'Hulu', 'Disnet', 'HolaMa', 'Amazon', 'PrimeVid'
    for i in range(n):
        cod = random.randint(100, 999)
        nom = random.choice(lista_nombres)
        tipo = random.randint(1, 15)
        cal = random.randint(0, 12)
        rep = random.randint(1, 999999)
        registro = Contenido(cod, nom, tipo, cal, rep)
        add_in_order(vector, registro)


def add_in_order(vector, registro):
    izq, der = 0, len(vector) - 1
    pos = 0

    while izq <= der:
        centro = (izq + der)//2
        
        if vector[centro].nombre == registro.nombre:
            pos = centro
            break

        if registro.nombre < vector[centro].nombre:
            der = centro - 1
        else:
            izq = centro + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [registro]


def generar_archivo(vector, fd, calif):
    m = open(fd, 'wb')
    for i in range(len(vector)):
        if vector[i].tipo != (4, 8, 12) and vector[i].calificacion > calif:
            pickle.dump(vector[i], m)
    if m.tell()> 0:
        print('Se ha creado correctamente')
    m.close()

def mostrar_archivo(fd):
    tot = 0

    if os.path.exists(fd) == False:
        print('El archivo', fd, 'no existe')
        return

    m = open(fd, 'rb')
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        reg = pickle.load(m)
        tot += reg.cant_rep
        print(to_string(reg))
    m.close()
    print('Total general de reproducciones:', tot)
