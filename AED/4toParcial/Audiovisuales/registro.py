
class Contenido:
    def __init__(self, codigo, nombre, tipo, calificacion, cant_reproducciones):
        self.codigo = codigo      
        self.nombre = nombre
        self.tipo = tipo
        self.calificacion = calificacion
        self.cant_rep = cant_reproducciones

def to_string(contenido):
    r = ''
    r += '| Codigo: {:>5}'.format(contenido.codigo)
    r += ' | Nombre: {:>15}'.format(contenido.nombre)
    r += ' | Tipo: {:>5}'.format(contenido.tipo)
    r += ' | Calificación: {:>5}'.format(contenido.calificacion)
    r += ' | Reproducciones: {:>15}'.format(contenido.cant_rep) + ' |'
    return r

#x = Contenido(54, 'Luluana', 10, 5, 7923847)
#print(to_string(x))












