# Ej2
print('Hello python')

list_num = []

bandera = False

while bandera == False:
    num = int(input('Ingresar numero: '))
    if(num == 0):
        bandera = True
    else:
        list_num.append(num)

promedio = 0

for i in list_num:
    promedio += i

promedio = promedio / len(list_num)

print(promedio)

