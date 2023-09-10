import random
import numpy as np
# ej1
 
# busca duplicado
def checkDuplicado(num, list):
    isvalid = True
    if num in list:
        isvalid = False # si encuentra duplicado pasa a FALSE
    return isvalid

# genera un num random
def numRandom(n):
    # config randomnum
    numMin = 0
    numMax = n * n
    num = random.randint(numMin,numMax)
    return num

def numerosRandom(n):
    cont = n * n
    listNum = []
    
    for ind in range(cont):
        num = numRandom(n)
        while(checkDuplicado(num, listNum) == False):
            num = numRandom(n)
        listNum.append(num)
    return listNum

def desordenada(n):
    tabla = np.empty((n, n), int)
    
    listNum = numerosRandom(n)
    cont = 0
    for fila in range(len(tabla)):
        #print('fila', fila) # muestra el num de fila
        for col in range(len(tabla[0])):
            #print('col', col) # muestra num de columna
            tabla[fila][col] = listNum[cont]
            cont += 1
    return tabla

def main():
    print('ej 1')
    n = int(input('ingresar num: '))
    tabla = desordenada(n)
    print(tabla)


main()