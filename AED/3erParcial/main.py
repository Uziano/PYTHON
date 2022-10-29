from registro import *
from funciones import *



def principal():
    vector = []
    vec_contador = []
    opc = -1
    while opc !=0:
        menu()
        opc = int(input('Ingrese la opcion: '))

        if opc == 1:
            n = int(input('Cantidad de figus: '))
            generador(n, vector)
            for i in range(len(vector)):
                print(to_string(vector[i]))

        elif opc == 2:
            pass

        elif opc == 3:
            pass

        elif opc == 4:
            pass

        elif opc == 0:
            print('Hasta Pronto')
        
        else:
            print('Ingrese una opcion válida')



if __name__ == '__main__':
    principal()
