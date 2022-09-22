#Inicializamos clase Libro

import random


class Libro():  # Clase

    def __init__(self, nombre, autor, estado, bio):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.bio = bio

    def get_nombre(self):  # Metodo get
        return self.nombre

    def set_nombre(self, nuevo_nombre):  # Metodo set
        self.nombre = nuevo_nombre
        return self.nombre

    def get_autor(self):  # Metodo get
        return self.autor

    def set_autor(self, nuevo_autor):  # Metodo set
        self.autor = nuevo_autor
        return self.autor

    def get_estado(self):  # Metodo get
        return self.estado

    def set_estado(self, nuevo_estado):  # Metodo set
        self.estado = nuevo_estado
        return self.estado

    def get_bio(self):  # Metodo get
        return self.bio

    def set_bio(self, nueva_bio):  # Metodo set
        self.bio = nueva_bio
        return self.bio

    def listar_libro(self):  # Metodo
        """
        Este metodo permite listar los libros ingresados
        """
        print('Nombre: ', self.nombre, end=' | ')
        print('Autor: ', self.autor, end=' | ')
        print('Estado: ', self.estado, end=' | ')
        print('Descripcion: ', self.bio)


# Funciones

def crear_libro(lista):
    """
    Esta funcion nos permite crear el objeto libro
    Args:
        lista (list): lista generica
    """
    # Crear libros de forma aleatoria
    lista_nombre = [
        'Cenicienta', 'Blanca Nieves', 'Tarzan', 'Ulises','Romeo y Julieta',
        'Homero'
    ]
    lista_autor = [
        'Hermanos Green', 'Clyde Geronimi', 'Edgar Rice Burroughs',
        'Shakespeare'
    ]
    lista_estado = ['Disponible', 'Alquilado']
    lista_bio = ['Cuento Infantil']

    nombre = random.choice(lista_nombre)
    autor = random.choice(lista_autor)
    estado = random.choice(lista_estado)
    bio = random.choice(lista_bio)

    libro_creado = Libro(nombre, autor, estado,
                         bio)  # Crea el objeto con los datos ingresados
    lista.append(libro_creado)  # Agrega el objeto a la lista


def cambiar_nombre(lista):
    """
    Esta funcion nos permite cambiarle el nombre al libro

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0:  #Me aseguro que la lista no este vacia al iniciar
        print("La lista de libros esta vacia. Por favor agregue libros. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Autor: ", libro.autor,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            #Anda------------------------------------------------------------------
            nombre_libro = input("Ingrese el nombre del libro a cambiar: ")

            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].nombre = input('Ingrese nuevo nombre: ')
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
            #----------------------------------------------------------------------


def cambiar_autor(lista):
    """
    Esta funcion nos permite cambiar el nombre del autor a traves del nombre de libro

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0:  #Me aseguro que la lista no este vacia al iniciar
        print("La lista de libros esta vacia. Por favor agregue libros. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Autor: ", libro.autor,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            #Anda-------------------------------------------------------------------------------
            nombre_libro = input(
                "Ingrese el nombre del libro que desea cambiarle el autor: ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].autor = input('Ingrese nuevo nombre del autor: ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
            #------------------------------------------------------------------------------------


def cambiar_estado(lista):
    """
    Esta funcion nos permite cambiar el estado al libro a traves del nombre de libro

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0: #Me aseguro que la lista no este vacia al iniciar 
        print("La lista de libros esta vacia. Por favor agregue libros. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Autor: ", libro.autor,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            #Anda-----------
            nombre_libro = input("Ingrese el nombre del libro que desea cambiarle el estado: ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].estado= input('Ingrese el nuevo estado del libro (DISPONIBLE O ALQUILADO): ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
            #---------------



def cambiar_bio(lista):
    """
    Esta funcion nos permite cambiar la descripcion del libro a traves del nombre de libro

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0: #Me aseguro que la lista no este vacia al iniciar 
        print("La lista de libros esta vacia. Por favor agregue libros. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Autor: ", libro.autor,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            #Anda-----------
            nombre_libro = input("Ingrese el nombre del libro que desea cambiarle la descripcion:  ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].bio= input('Ingrese la nueva descripcion del libro: ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
            #---------------