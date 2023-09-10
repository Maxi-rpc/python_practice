# ej3
def validarCar(palabra):
    valid = True
    if(len(palabra) > 5):
        valid = False
    return valid

def buscarVoc(palabra):
    vocales = ['A', 'E', 'I', 'O', 'U']
    voc = []
    cons = []
    for letra in palabra:
        if(letra in vocales):
            voc.append(letra)
        else:
            cons.append(letra)
    print(voc)
    print(cons)

    cont = len(cons)
    palabraCon = ''
    for i in range(len(palabra)):
        print(palabraCon)

EJ perro, se toma letra repetida?
SEXTO texos


def main():
    print('ej 3')
    palabra = ''

    list_palabras = []
    while(palabra != 'FINAL'):
        palabra = input('Ingresar palabra: ')

        while(validarCar(palabra) != True):
            palabra = input('Ingresar palabra: ')
        
        list_palabras.append(palabra)
        buscarVoc(palabra)
    
    


main()

