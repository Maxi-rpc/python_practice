import numpy as np
# ej1
 
# busca duplicado
def checkDuplicado(num, list):
    isvalid = True
    if num in list:
        isvalid = False # si encuentra duplicado pasa a FALSE
    return isvalid

def desordenada(n):
    tabla = []
    for fila in range(len(tabla)):
        #print('fila', fila) # muestra el num de fila
        for col in range(len(tabla[0])):
            #print('col', col) # muestra num de columna
            print(tabla[fila][col]) 

def main():
    print('ej 1')
    a = np.arange(6 )
    print(a)


main()