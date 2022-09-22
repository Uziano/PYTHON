from soporte import *

v = vector_unknown_range(300000)
num = []
cont = []

#print(len(num))    
# determinar el valor modal del vector v original. 
# 3 se le pedirá que informe también la frecuencia del valor modal
# misma frecuencia máxima), entonces informe un 0(cero) cuando se le pida el valor modal.

may = 0

for i,elemento_vec in enumerate(v):
    if elemento_vec in num:
        j = num.index(elemento_vec)
        cont[j] += 1
    else:
        num.append(elemento_vec)
        cont.append(1)
print(len(v))
# print(num)
# print(cont)

for elemento_modal in cont:
    if elemento_modal > may:
        flag_may = False
        may = elemento_modal

    elif elemento_modal == may:
        flag_may = True

if flag_may:
    may = 0
    print(f'El modal es: 0')
else:
    modal = cont.index(may)
    print(f'El modal es {num[modal]}')
    print(f'La frecuencia modal es de: {may}')







