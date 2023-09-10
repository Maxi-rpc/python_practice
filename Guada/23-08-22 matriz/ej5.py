# crear tabla 5x15 
from pprint import pprint
from tabulate import tabulate
mercado = [
    [0, 0, 0, 0, 0], # suc 1
    [0, 0, 0, 0, 0], # suc 2
    [0, 0, 0, 0, 0], # suc 3
    [0, 0, 0, 0, 0] # suc 4
]
# completar articulos de cada sucursal del mercado
def cargarArticulos():
    for fila in range(len(mercado)):
        #print('fila', fila) # muestra el num de fila
        print('sucursal n:', fila + 1)
        for col in range(len(mercado[0])):
            #print('col', col) # muestra num de columna
            #print(mercado[fila][col])
            cantArt = int(input(f'indicar cantidad del articulo {col + 1}: '))
            mercado[fila][col] = cantArt

# cantidad total de cada articulo
def punto1():
    list_articulos = [0, 0, 0, 0, 0]
    for fila in range(len(mercado)):
        for col in range(len(mercado[0])):
            list_articulos[col] += mercado[fila][col]
    print('cantidad total de cada articulo')
    print(list_articulos)

# la cantidad de art en la suc 2  
def punto2():
    cantDeArtSuc = 0
    suc = 1 # posicion
    for fila in range(len(mercado)):
        for col in range(len(mercado[0])):
            if(fila == suc):
                cantDeArtSuc += mercado[fila][col]
    print('Cantidad de articulos sucursal 2: ',cantDeArtSuc)

# la cantidad de art 3 en la suc 1 
def punto3():
    cantDeArt = 0
    suc = 0 # posicion
    art = 2 # posicion
    cantDeArt = mercado[suc][art]
    print('Cantidad de articulos 3 sucursal 1: ',cantDeArt)

# la recaudacion total de cada sucursal
def punto4():
    list_suc = [0, 0, 0, 0]
    for fila in range(len(mercado)):
        for col in range(len(mercado[0])):
            list_suc[fila] += mercado[fila][col]
    print('Recaudacion total de cada sucursal')
    print(list_suc)

# recaudacion total de la empresa
def punto5():
    total = 0
    for fila in range(len(mercado)):
        for col in range(len(mercado[0])):
            total += mercado[fila][col]
    print('Recaudacion total de la empresa', total)

# sucursal de mayor recaudacion
def punto6():
    list_suc = [0, 0, 0, 0]
    for fila in range(len(mercado)):
        for col in range(len(mercado[0])):
            list_suc[fila] += mercado[fila][col]
    mayor = 0
    sucMayor = 0
    cont = 0
    for suc in list_suc:
        if(suc > mayor):
            mayor = suc
            sucMayor = cont
        cont += 1
    print('Sucursal con mayor recaudacion', sucMayor + 1)

def main():
    print('ej5')
    
    cargarArticulos()
    #pprint(mercado)
    print(tabulate(mercado, headers=['art-1', 'art-2', 'art-3', 'art-4', 'art-5']))
    punto1()
    punto2()
    punto3()
    punto4()
    punto5()
    punto6()


main()