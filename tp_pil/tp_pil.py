import registro as re

def menu():  
  print("""
------------------------ MENU PRINCIPAL ------------------------
\t Por favor ingrese una opcion:
\t 1. Crear un libro
\t 2. Listar libros
\t 3. Cambiar nombre del libro 
\t 4. Cambiar nombre del autor 
\t 5. Cambiar estado del libro (DISPONIBLE O ALQUILADO) 
\t 6. Cambiar descripcion del libro 
\t 7. Salir
""")
  print("-"*64)
  print('')

def validar_libros(lista):
  """
  Esta función nos permite verificar si la lista esta vacia. 
  Si la lista esta vacia pedira que se carguen libros, sino imprimira por pantalla los libros ya cargados.
  Args:
      lista (list): lista generica
  """
  if len(lista) < 1:
    print('Debe cargar libros primero')
  else:
    for i in lista:
        i.listar_libro()

lista = []
opcion = -1
while opcion != '7':
    menu()
    opcion = input('Elija una opcion: ')

    if (opcion == '1'):
      cant = int(input('Ingrese cantidad de libros a cargar: '))
      for i in range(cant):
        re.crear_libro(lista)
      print('Se han cargado libros!')
      print('Total de libros cargados: ', + lista.__len__())
       
    elif (opcion == '2'):
      validar_libros(lista)
    
    elif (opcion == '3'):
      re.cambiar_nombre(lista)

    elif (opcion == '4'):
      re.cambiar_autor(lista)

    elif (opcion == '5'):
      re.cambiar_estado(lista)
      
    elif (opcion == '6'):
      re.cambiar_bio(lista)

    else:
      print('¡Gracias por utilizar este programa!')   