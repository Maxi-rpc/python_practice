from random import randint
list_pa = ['pepe','pepa','tete','pepe']

# empieza funcion
def duplicado(lista_palabra):
    esduplicado = False
    list_sin_dup = []
    for p in lista_palabra:
        if(p in list_sin_dup):
            esduplicado = True
        else:
            list_sin_dup.append(p)
    return esduplicado
# termina funcion

def listaRandom():
    lista_random = []
    for n in range(23):
        n = randint(1,100)
        lista_random.append(n)

    return lista_random

listaNueva = listaRandom()

# empieza codigo main
lista_a_llenar = []
cosito = True

while cosito == True:
    palabra = input('Ingresar palabras para la lista: ')

    if(palabra == 'fin'):
        cosito = False
    else:
        lista_a_llenar.append(palabra)

print(duplicado(lista_a_llenar))