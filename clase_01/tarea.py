#Escribir un programa que reciba una palabra y desplegar la cant de * de letras.
#Hacer del punto 3 un diccionario

def ejercicio_03_04():
    palabra = str(input('Ingrese la palabra a convertir: '))
    palabra_convertida = len(palabra) * '*'

    usuario = {
        1 : palabra,
        2 : palabra_convertida
    }

    print(palabra, palabra_convertida)
    print(usuario)
    

def main():
    ejercicio_03_04()
    
if __name__ == '__main__':
    main()