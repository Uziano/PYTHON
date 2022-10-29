import pickle
import os.path
import random
import re
from registro import *
lista_nombres = ['Jose', 'Nico', 'Nahuel', 'Diego', 'Fernando']

def menu():
    print('1 - Cargar Figuritas')
    print('2 - Mostrar mayores a v')
    print('3 - Figuritas por Pais')
    print('4 - Cambiar valor figurita')
    print('0 - Salir')

def generador(cantidad, vector):
    for i in range(cantidad):
        
        pais = random.randint(1, 32)
        numero = random.randint(1, 19)
        nombre = random.choice(lista_nombres)
        posicion = random.randint(1, 3)
            #0: arquero, 1: defensor, 2: volante, 3: delantero
        valor = random.randint(1, 1000)
            #cualquier entero

        x = Figurita(pais, numero, nombre, posicion, valor)
        vector.append(x)
            #Al usar append no retorno nada
    print('Se han agregado figuritas...')

# De aca para abajo estoy practicando lo dado el lunes

def add_in_order(vector, registro):
    izq, der = 0, len(vector) - 1
    pos = 0

    while izq <= der:
        centro = (izq + der) // 2

        if vector[centro] == registro:
            pos = centro
            break

        if registro < vector[centro]:
            der = centro - 1
        else:
            izq = centro + 1 

    if izq > der:
        pos = izq

    vector[pos:pos] = [registro]


        # Esto seria con la caracteristica para ordenar
        #   if vector[centro].|||something|||== registro.something:
        #        posicion = centro
        #        break

        #   if registro.something < vector[centro].something:
        #       der = centro - 1
        #   else:
        #       izq = centro + 1 


def crear_registro(vector, n):
    servicios = 'youtube', 'tiktok', 'amazon', 'huli', 'disney'
    for i in range(n):
        codigo = random.randint(100, 999)
        nombre = random.choice(servicios)
        tipo = random.randint(1, 15)
        calificacion = random.randint(1000,2000)

        registro = 0
            #Relleno, deberia ser la clase

        
        add_in_order(vector, registro)
            # Ahora esto es distinto(antes era vector.append)

def linea_search(vector, n):
    v = []
    for i in range(len(vector)):
        if vector[i].something > n:
            v.append(v[i])
    return v

def mostrar_registro(vector):
    print()
    for i in vector:
        print(to_string(vector))


def conteo(vector, cantidad_buscada):
    v = [0] * 32
    for i in range(len(vector)):
        if v[i].cantidad > cantidad_buscada:
            v[i].acumuladores += 1
    return v

def crear_archivo(vec, fd, c):
    condiciones = 'Las del ejerciocio para filtrar para pickle'
        #si es que las hay

    m = open(fd, 'wb')

    for i in range(len(vec)):
        if condiciones:
            pickle.dump(vec[i], m)

    m.close()
    print('Se creo correctamente')

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('\no se encontró el archivo')
        return
    m = open(fd,'rb')
    t = os.path.getsize(fd)

    while m.tell() < t:
        linea = pickle.load(m)
        print(to_string(linea))
        total_rep += linea.something
            #Something es la cant de reproducciones

    m.close()
    print('\n total de repros es de: ', total_rep)




