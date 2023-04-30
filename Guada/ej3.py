# Ej2
print('Hello python')

list_palabras = []

bandera = True

while bandera:
    palabra = str(input('Ingresar una palabra: '))

    if(palabra == 'FIN'):
        bandera = False
    else:
        list_palabras.append(palabra)

palabra_mas_larga = ''

for i in list_palabras:
    
    if(len(i) > len(palabra_mas_larga)):
        palabra_mas_larga = i

print(palabra_mas_larga)
