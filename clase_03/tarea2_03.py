#Idear un programa que solicite al usuario dos números enteros y el programa
#deberá retornar aquellos números pares que se encuentren dentro del rango
#formado entre los números ingresados.

opc = -1
while opc != 0:
    
    print('1 - Hacer Lista')
    print('0 - SALIR')
    opc = (input('\nIngrese la opcion: \n -->'))

    if opc == 1:
        #Solicito rango a usar:
        a = int(input('Ingrese numero 1: '))
        b = int(input('Ingrese numero 2: '))

        #Valido que sean pares:
        if (a % 2) != 0:
            a += 1
        if (b % 2) != 0:
            b += 1
        print(list(range(a,b,2)))

    elif opc == 0:
        print('Nos vemos!')

    else: 
        print('Elija una opcion valida\n')

