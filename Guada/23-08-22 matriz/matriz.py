matriz = [                  # col1 col2 col3 col4 col5
    [0, 3, 1, 2, 1], # fila 1
    [1, 0, 3, 2, 3], # fila 2
    [0, 2, 0, 1, 1], # fila 3
    [1, 0, 2, 0, 1], # fila 4
    [3, 4, 1, 2, 0]  # fila 5
]

# recorrer matriz
for fila in range(len(matriz)):
    print('fila', fila) # muestra el num de fila
    for col in range(len(matriz[0])):
        print('col', col) # muestra num de columna
        print(matriz[fila][col]) # muestra valor de la fila y col