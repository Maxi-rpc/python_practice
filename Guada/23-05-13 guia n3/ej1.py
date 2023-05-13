print('Ejercicio 1')


# validaciones FUNCION: solo alfabetico o espacios min 10 y max 30 caracteres
def validar_parrafo(parraf):
    cosito = False
    min = 10
    max = 30
    canCaracteres = len(parraf)
    #print(canCaracteres)
    if(canCaracteres >= min) and (canCaracteres <= max):
        cosito = True
    return cosito

def buscar_rep(letra,parraf):
    contador = 0
    dic_letra = {}
    for let in parraf:
       if(let == letra):
           contador = contador + 1
           
    dic_letra['letra'] = letra
    dic_letra['cantidad'] = contador
    return dic_letra
                   


# ingresar parrafo 
parrafo = str(input('Ingrese un parrafo: '))

parrafo_validar = validar_parrafo(parrafo)

while parrafo_validar == False:
    parrafo = str(input('Ingrese un parrafo: '))
    parrafo_validar = validar_parrafo(parrafo)

lista_letras_repetidas = []

for caracter in parrafo:
    letra_repetida = buscar_rep(caracter, parrafo)
    lista_letras_repetidas.append(letra_repetida)

lista_dup = []
for l in lista_letras_repetidas:
    if not (l in lista_dup):
        lista_dup.append(l)

# fin ingreso, mostrar letra mas repetida
print(lista_dup)