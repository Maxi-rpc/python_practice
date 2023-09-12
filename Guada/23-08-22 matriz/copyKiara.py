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
    

    if len(voc) > len(cons):
        
        orden = (cons[-1] + voc[0] + cons[-2] + voc[1] + voc[2])
        print(orden)
    else:
        orden = (cons[-1] + voc[0] + cons[-2] + voc[1] + cons[-3])
        print(orden)

def main():
    print('\n ejercicio 3')
    print('NOTA: Las palabras ingresadas deben estar en mayuscula!!!!')
    palabra = ''

    list_palabras = []
    while(palabra != 'FINAL'):
        palabra = input('Ingresar palabra: ')
        while(validarCar(palabra) != True):
            palabra = input('Ingresar palabra: ')
        if(palabra != 'FINAL'):
            list_palabras.append(palabra)
    
    for pal in list_palabras:
        buscarVoc(pal)
    

main()