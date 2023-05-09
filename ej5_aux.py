lista_uno = []
palabra_listauno = ''
cosito = True

while cosito == True:
    palabra_listauno = input('Ingrese una palabra para la lista: ')

    if(palabra_listauno == 'fin'):
        cosito = False

    # elif not (palabra_listauno in lista_uno):
    #     lista_uno.append(palabra_listauno)
    
    else:
        lista_uno.append(palabra_listauno)
print(lista_uno)

lista_final = []
for palabra in lista_uno:
    if not (palabra in lista_final):
        lista_final.append(palabra)

print(lista_final)