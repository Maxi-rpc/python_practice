# generar num random para tabla de bingo 15 num random
import random
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

# busca duplicado
def checkDuplicado(num):
    isvalid = True
    for fila in tabla:
        if num in fila:
            isvalid = False # si encuentra duplicado pasa a FALSE

    return isvalid

for fila in range(len(tabla)):
    # print(fila) # muestra el num de fila
    for col in range(len(tabla[0])):
        # print(celda) # muestra num de columna
        numR = numRandom()
        while (checkDuplicado(numR) == False): # si es FALSE vuelve a repetir la asignacion
            numR = numRandom()
        tabla[fila][col] = numR

print(tabla)

tablaOrd = sorted(tabla, key=lambda x:x[0])

print()
print(tablaOrd)