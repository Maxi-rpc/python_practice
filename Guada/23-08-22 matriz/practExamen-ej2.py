import random
import numpy as np
from pprint import pprint
from tabulate import tabulate
# ej2

matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

matriz_solucion = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]


# genera un num random
def numRandom():
    numMin = 0
    numMax = 8
    num = random.randint(numMin,numMax)
    return num

def checkDuplicado(num, listNum):
    isvalid = True
    if num in listNum:
        isvalid = False # si encuentra duplicado pasa a FALSE
    return isvalid

def cargar_datos():
    listaNum = []
    for n in range(9):
        num = numRandom()
        while (checkDuplicado(num, listaNum)== False):
            num = numRandom()
        listaNum.append(num)

    cont = 0
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            matriz[fila][col] = listaNum[cont]
            cont += 1 

def buscar_pos(ficha):
    pos = {
        'fila': 0,
        'col': 0
    }
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
           if(matriz[fila][col] == ficha):
               pos['fila'] = fila
               pos['col'] = col
    return pos

def mover_ficha(ficha):
    vacio = 0
    pos_origen = buscar_pos(ficha)
    pos_destino = buscar_pos(vacio)
    # asignar destino
    matriz[pos_destino['fila']][pos_destino['col']] = ficha
    # asignar destino
    matriz[pos_origen['fila']][pos_origen['col']] = vacio

def validar_solucion():
    solucion = True
    for fila in range(len(matriz_solucion)):
        for col in range(len(matriz_solucion[0])):
           if(matriz_solucion[fila][col] != matriz[fila][col]):
               solucion = False
    print(str(solucion))
    return solucion

def main():
    print('ej 2')
    cargar_datos()
    contador_turnos = 0
    print(tabulate(matriz))
    
    print('Turno:', contador_turnos)
    num = int(input('Indicar Numero a mover: '))
    mover_ficha(num)
    print(tabulate(matriz))

    while(validar_solucion() != True):
        print('Turno:', contador_turnos)
        num = int(input('Indicar Numero a mover: '))
        mover_ficha(num)
        print(tabulate(matriz))
        contador_turnos += 1

    print('Cantidad de turnos totales:', contador_turnos)
    print('Fin del juego')
    
   


main()