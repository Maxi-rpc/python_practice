print('ej1')
# kiara code
# nombre primaria
nombres_primario = []  

cosito = True

while cosito == True:
    nombres_primaria = input('ingresar nombre de pila nivel primario: ')

    if (nombres_primaria == 'x' ):
         cosito = False
    else: 
        nombres_primario.append(nombres_primaria)

print('el ingreso de nombres de nivel primario a finalizado')

# nombre secundaria
nombres_secundaria = []

while cosito == False:
    nombres_secundario = input('ingresar nombre de pila nivel secundario: ')

    if (nombres_secundario == 'x' ):
        cosito = True
    else:
        nombres_secundaria.append(nombres_secundario)

print('el ingreso de nombres nivel secundario a finalizado')

## maxi code
print('----------')
print('Nombres de primaria y secundaria sin repetir')
nombres_repetidos = []
nombres_no_repetidos = []
for i in nombres_primario:
    print(i)
    if not (i in nombres_secundaria):
        nombres_no_repetidos.append(i)

for n in nombres_secundaria:
    if not (n in nombres_primario):
        print(n)
    else:
        nombres_repetidos.append(n)
print('----------')
print('nombres repetidos: ')
print(nombres_repetidos)

print('nombres NO repetidos de primaria: ')
print(nombres_no_repetidos)