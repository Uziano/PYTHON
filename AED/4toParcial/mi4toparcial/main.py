import pickle
import os.path
from registro import *

def validar_positivo(n):
    while n <= 0:
        n = int(input('Ingrese una cantidad válida: '))
    return n

def reemplazo(vec):
    #Le pido perdon pero anda...jaja
    vec_reemplazado = vec
    for i in range(len(vec_reemplazado)):
        if vec_reemplazado[i].tamaño == 1:
            vec_reemplazado[i].tamaño = 'Subcompacto'
        elif vec_reemplazado[i].tamaño == 2:
            vec_reemplazado[i].tamaño = 'Compacto'
        elif vec_reemplazado[i].tamaño == 3:
            vec_reemplazado[i].tamaño = 'Mediano'
        elif vec_reemplazado[i].tamaño == 4:
            vec_reemplazado[i].tamaño = 'Grande'

        if vec_reemplazado[i].tipo == 0:
            vec_reemplazado[i].tipo = 'Nafta'
        elif vec_reemplazado[i].tipo == 1:
            vec_reemplazado[i].tipo = 'Gasoil'
        elif vec_reemplazado[i].tipo == 2:
            vec_reemplazado[i].tipo = 'GNC'
        elif vec_reemplazado[i].tipo == 3:
            vec_reemplazado[i].tipo = 'Electrico'
        elif vec_reemplazado[i].tipo == 4:
            vec_reemplazado[i].tipo = 'Hidrogeno'
    return vec_reemplazado

def menu():
    print(' \nMENU DE OPCIONES ')
    print('1 - Cargar Vehiculos ')
    print('2 - Mostrar Vehiculos c descripcion')
    print('3 - Buscar por id')
    print('4 - Generar Archivo')
    print('5 - Mostrar Archivo y costo promedio')
    print('0 - Salir')

def principal():
    opcion = -1
    v = []
    NOMBRE_ARCHIVO = 'Autos.dat'
    while opcion != 0:
        menu()
        opcion = int(input('Ingrese su opcion deseada: '))

        if opcion == 1:
            n = int(input('Ingrese cantidad de vehiculos: '))
            n = validar_positivo(n)
            generador(v, n)

        elif opcion == 2:
            vec_impresion = reemplazo(v)
            for i in range(len(vec_impresion)):
                print(to_string(vec_impresion[i]))

        elif opcion == 3:
            flagNot = True
            b = int(input('Ingrese ID: '))
            for i in range(len(v)):
                if v[i].id == b:
                    print('Se encontró id: ')
                    print(to_string(v[i]))
                    flagNot = False
            if flagNot == True:
                print('No se encontró id...')

        elif opcion == 4:
            m = open(NOMBRE_ARCHIVO, 'wb')
            for i in range(len(v)):
                if v[i].tamaño == 3 or v[i].tamaño == 4 or v[i].tamaño == 'Mediano' or v[i].tamaño == 'Grande':
                    pickle.dump(v[i], m)
            if os.path.exists(NOMBRE_ARCHIVO):
                print('Archivo Creado')
            m.close()

        elif opcion == 5:
            if not os.path.exists(NOMBRE_ARCHIVO):
                print("El archivo no existe")
            else:
                m = open(NOMBRE_ARCHIVO, 'rb')
                size = os.path.getsize(NOMBRE_ARCHIVO)
                cantidad = suma = 0

                while m.tell() < size:
                    vehiculo = pickle.load(m)
                    print(to_string(vehiculo))

                    suma += vehiculo.costo
                    cantidad += 1

                if cantidad < 0:
                    print('Debe cargar registros primero')
                else:
                    promedio = suma / cantidad
                    print(f'El promedio de costo es {promedio}')
            m.close()

        elif opcion == 0:
            print('Nos vemos!')
        else:
            print('Ingrese una opcion válida...')

if __name__ == '__main__':
    principal()