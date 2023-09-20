##
verb_inf = [ 'ar', 'er', 'ir' ]
list_palabras = []
list_verbos = []

def parsearOracion(oracion):
    palabras = oracion.split()
    return palabras
    
def separarVerbos(palabras):
    cont = len(palabras)
    ind = 0
    while ind < cont:
        texto = palabras[ind]
        if texto[-2:] in verb_inf:
            print(texto)
            resp = int(input('Es un verbo? 1-Si 0-No : '))
            if(resp == 1):
                list_verbos.append(texto)
        ind = ind + 1

def main():
    print('Ej1')
    oracion = str(input('Ingresar una oracion: '))
    cant = len(oracion)
    while cant > 50:
        oracion = str(input('Ingresar una oracion: '))
        cant = len(oracion)
    
    list_palabras = parsearOracion(oracion)
    separarVerbos(list_palabras)
    print('Verbos: ')
    print(list_verbos)

main()