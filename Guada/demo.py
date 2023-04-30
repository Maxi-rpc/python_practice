print('Hello python')

list_palabras = []
palabra_mas_larga = ''

for i in range(3):
    palabra = input('Ingrese una palabra: ')
    longitud = len(palabra)
    print('La palabra ingresada tiene', longitud, 'caracteres')
    
    list_palabras.append(palabra)

for p in list_palabras:
    if(len(p) > len(palabra_mas_larga)):
        palabra_mas_larga = p

print('La palabra mas larga es: ', palabra_mas_larga)

# otra aleternativa

for i in range(3):
    palabra = input('Ingrese una palabra: ')
    longitud = len(palabra)
    print('La palabra ingresada tiene', longitud, 'caracteres')
    
    if(longitud > len(palabra_mas_larga)):
        palabra_mas_larga = palabra

print('La palabra mas larga es: ', palabra_mas_larga)