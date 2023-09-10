# generar num random para tabla de bingo 15 num random
import random
import pprint
from tabulate import tabulate
# 5 filas 3 col
tabla = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
] 

# config randomnum
numMin = 1
numMax = 25
# genera un num random
def numRandom():
    num = random.randint(numMin,numMax)
    return num

# lista vacia
listNum = []
# busca duplicado
def checkDuplicado(num):
    isvalid = True
    if num in listNum:
        isvalid = False # si encuentra duplicado pasa a FALSE
    return isvalid
# completa lista
for n in range(15):
    numR = numRandom()
    while (checkDuplicado(numR) == False): # si es FALSE vuelve a repetir la asignacion
        numR = numRandom()
    listNum.append(numR)
# ordena lista
listNum.sort()
#print(listNum) # muestra lista ordenada

# asignamos a la matriz
cont = 0
for fila in range(len(tabla)):
    # print(fila) # muestra el num de fila
    for col in range(len(tabla[0])):
        # print(celda) # muestra num de columna
        tabla[fila][col] = listNum[cont]
        cont += 1 # le agrego 1 a la posicion de la listNum

#print(tabla)

print(tabulate(tabla, headers=['col1', 'col2', 'col3']))