print('ejercicio 3')

#números de 5 dígitos, en un vector, hasta que uno de ellos sea negativo.
num = str(input('ingresar numero de cinco digitos: '))

def validar_digitos(numero):
    esvalido = True
    if (len(numero) > 5) or ('-' in num):
        esvalido = False
    return esvalido

print(num)
print(validar_digitos(num))

#descomponer los números


# agrupando los dígitos pares en un vector y los impares
lista_par = []
lista_impar = []

def agrupar(numeros):
    for i in numeros:
        numerito = int(i)
        if (numerito % 2 == 0):
            lista_par.append(numerito)
        else:
            lista_impar.append(numerito)

agrupar(num)
print('los numeros pares ingresados son: ')
print(lista_par)
print('los numeros impares ingresados son: ')
print(lista_impar)

#se deben mostrar los resultados de las sumas de los números de estos últimos 
# vectores por posiciones contiguas (el 1ro de los pares con el 1ro de los impares, y así sucesivamente).

lista_resultado = []

if (len(lista_par) > len(lista_impar)):
    dif = len(lista_par) - len(lista_impar)
    for i in range(dif):
        lista_impar.append(0)


    for x in range(len(lista_par)):
        suma = lista_par[x] + lista_impar[x]
        lista_resultado.append(suma)
else: 
    dif = len(lista_impar) - len(lista_par)
    for i in range(dif):
        lista_par.append(0)


    for x in range(len(lista_impar)):
        suma = lista_impar[x] + lista_par[x]
        lista_resultado.append(suma)

print('el resultado de la suma de los pares con impares es: ')
print(lista_resultado)        

