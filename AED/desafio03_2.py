from soporte import *

v = vector_known_range(300000)
num = []
cont = [0] * len(v)
cont2 = 0
for i,elemento_vec in enumerate(v):
    if elemento_vec in num:
        j = num.index(elemento_vec)
        cont[j] += 1
    else:
        num.append(elemento_vec)
    
print(len(cont))

# 0.)  Cree un arreglo c de 300000 casillas, inicializadas en cero.
# 1.)  Para cada número x del vector v de entrada:
#           1.1) Incremente en uno la casilla c[x]
# 2.)  Mostrar la cantidad de casilleros diferentes de cero que quedaron en el arreglo c.
