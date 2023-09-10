# crear matriz y completar la diagonal con 1 el resto con 0
from pprint import pprint
import numpy as np
def ejemp():
# ejemplo de matriz a crear 5x5
    diagonal = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    cont = 0
    for fila in range(len(diagonal)):
        #print('fila', fila) # muestra el num de fila
        for col in range(len(diagonal[0])):
            #print('col', col) # muestra num de columna
            #print(diagonal[fila][col]) 
            if(fila == cont and col == cont):
                #print(cont)
                diagonal[fila][col] = 1
        cont += 1

    pprint(diagonal)

def asignarValor(matriz, value):
    cont = 0
    for fila in range(len(matriz)):
        #print('fila', fila) # muestra el num de fila
        for col in range(len(matriz[0])):
            #print('col', col) # muestra num de columna
            #print(diagonal[fila][col]) 
            if(fila == cont and col == cont):
                #print(cont)
                matriz[fila][col] = value
            else:
                matriz[fila][col] = 0
        cont += 1
    return matriz

def ej2():
    #diagonal = np.eye(5) # crea matriz con diagonal 1
    diagonal = np.empty((5,5), int)
    diagonal = asignarValor(diagonal, 1)
    pprint(diagonal)

ej2()