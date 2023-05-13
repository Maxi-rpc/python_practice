print('Ejercicio 2')

# ingresar en un vector 15 elementos
lista_num = []
cant_num = 3 # debe ir 15

# validar numéricos enteros, positivos y menores a 21.
def validar_num(num):
    esValido = False
    if(num >= 0) and (num <= 21):
        esValido = True
    return esValido

# mostrar en una matriz el factorial de cada uno de los elementos ingresados en el vector
def fact(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

# funcion para el numero mas repetido
def mas_repetido(lista_num):
    lista_duplicado = []
    for i in lista_num:
        num = buscar_rep(i, lista_num)
        if not(num in lista_duplicado):
            lista_duplicado.append(num)

    mas_rep = {}
    mas_rep['cantidad'] = 0
    for n in lista_duplicado:
        if (n['cantidad'] > mas_rep['cantidad']):
            mas_rep = n
    print(mas_rep)

def buscar_rep(num, lista_num):
    contador = 0
    dic_num = {}
    for n in lista_num:
       if(n == num):
           contador = contador + 1
           
    dic_num['numero'] = num
    dic_num['cantidad'] = contador
    return dic_num

lista_matriz = []

for i in range(cant_num):
    num = int(input('Ingresar numero: '))
    while validar_num(num) == False:
        print('Ingresar un numero positivo y menor a 21')
        num = int(input('Ingresar numero: '))
    
    lista_num.append(num)
    num_fac = fact(num)

    matriz = [num, num_fac]
    lista_matriz.append(matriz)

print('el numero y su factorial es: ')
print(lista_matriz)

# informar cuál fue el número más repetido.
print('el numero mas repetido es: ')
mas_repetido(lista_matriz)




