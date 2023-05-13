'''
Eiercicio 1: Queremos guardar la temperatura minima y måxima de 5 dias. Realiza
un programa que de la siguiente informaciön:
• La temperatura media de cada dia
• Los dias con menos temperatura
'''

lista_temp_max = []
lista_temp_min = []
lista_temp_media = []
dias = 5

for i in range(dias):
    temp_max = float(input('ingresar temp max: '))
    temp_min = float(input('ingresar temp min: '))
    temp_prom = temp_max + temp_min
    temp_prom = temp_prom / 2

    lista_temp_max.append(temp_max)
    lista_temp_min.append(temp_min)
    lista_temp_media.append(temp_prom)
    

print('Temperatura max')
print(lista_temp_max)
print('Temperatura min')
print(lista_temp_min)
print('Temperatura promedio')
print(lista_temp_media)

tempMin = 10
for x in range(dias):
    dia = x+1
    if(lista_temp_min[x] <= tempMin):
        print(f'El dia: {dia} tuvo temperatura menor o igual a {tempMin}')
        print(lista_temp_min[x])

