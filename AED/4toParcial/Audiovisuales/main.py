import pickle
import os.path
from registro import *
from funcionesAudio import *


def principal():
    opc = -1
    v = []
    while opc != 0:
        menu()
        opc = int(input('Ingrese la opcion deseada: ')) 

        if opc == 1:
            n = int(input('\n Ingrese cantidad a crear: '))
            generador(v,n)
        
        elif len(v) == 0:
            #Este es el control
            print('El vector no esta cargado...')
        
        elif opc == 2:
            c = int(input('\n Ingrese minimo de reproducciones: '))
            for i in range(len(v)):
                if v[i].cant_rep > c:
                    print(to_string(v[i]))

        elif opc == 3:
            pass
        
        elif opc == 4:
            fd = 'registrosAudio.dat'
            calif = int(input('Ingrese calificacion a guardar: '))
            generar_archivo(v, fd, calif)
        
        elif opc == 5:
            mostrar_archivo(fd)
        
        if opc == 0:
            print('Nos vemos!')

if __name__ == '__main__':
    principal()