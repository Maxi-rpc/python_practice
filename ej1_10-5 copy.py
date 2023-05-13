'''
Eiercicio 1: Queremos guardar la temperatura minima y måxima de 5 dias. Realiza
un programa que de la siguiente informaciön:
• La temperatura media de cada dia
• Los dias con menos temperatura <5
'''
dias = 2
lista_temp = []
temp_menor = 10.0

for i in range(dias):
    temp_max = float(input('ingresar temp max: '))
    temp_min = float(input('ingresar temp min: '))

    ## nuevo codigo
    temp_dia = {
        'index': i,
        'min': 0,
        'max': 0,
        'media': 0
    }

    temp_dia['max'] = temp_max
    temp_dia['min'] = temp_min

    temp_prom = temp_max + temp_min
    temp_prom = temp_prom / 2
    temp_dia['media'] = temp_prom

    lista_temp.append(temp_dia)

#print(lista_temp)

for dia in lista_temp:
    if(dia['min'] < temp_menor):
        dia_mostrar = dia['index'] + 1
        print(f"Dia: {dia_mostrar} temperatura minima: {dia['min']}")
        


    


