opcion = -1
dinero_en_cuenta = 0
while opcion != 0:
    print('-'*17)
    print('Menu de Opciones')
    print('-'*17)
    print('1-Deposito.\n2-Extracción.\n3-Transferencia.\n4-Estado Cuenta.\n0-Salir.')
    opcion = int(input('\nIngrese la opcion: \n -->'))

    if opcion == 1:
        deposito = int(input('Ingrese Monto a depositar: '))
        dinero_en_cuenta += deposito

    elif opcion == 2:
        if dinero_en_cuenta > 0:
            extraccion = int(input('Ingrese Monto a extraer: '))
            #Valido no sacar mas de lo que tengo
            while extraccion > dinero_en_cuenta:
                extraccion = int(input('Ingrese Monto no mayor a sus fondos: '))
            dinero_en_cuenta -= extraccion
        else:
            print('Debe primero ingresar dinero.')

    elif opcion == 3:
        if dinero_en_cuenta > 0:
            transferencia = int(input('Ingrese Monto a transferir: '))
            while transferencia > dinero_en_cuenta:
                transferencia = int(input('Ingrese Monto no mayor a sus fondos: '))
            dinero_en_cuenta -= transferencia
        else:
            print('No puede tranferir si no tiene dineros...')
        
    elif opcion == 4:
        print(f'Su saldo actual es de: ${dinero_en_cuenta}')

    elif opcion == 0:
        print('Nos vemos!')

    else: 
        print('Elija una opcion valida\n')


