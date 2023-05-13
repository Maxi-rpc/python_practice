'''
Ejercicio 2: De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, 
y los kilómetros que conducen cada día de la semana.

Para guardar esta información se van a utilizar dos vectores:
Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que han realizado.
'''

def suma_kilometros(lista_km):
    total = 0
    for km in lista_km:
        total = total + km
    return total



lista_conductores = []
dias = 7

cosito = True

while cosito == True:
    nombres_conductores = []
    kilometros_totales = []
    nombre = str(input('ingresar el nombre del conductor: '))

    if (nombre == 'fin'):
        cosito = False
    else:    
        nombres_conductores.append(nombre)
    
        for x in range (dias):
            km = int(input('ingresar los kilometros realizados en el dia: '))
            kilometros_totales.append(km)
        nombres_conductores.append(kilometros_totales)
        km_totales = suma_kilometros(kilometros_totales)
        nombres_conductores.append(km_totales)
        lista_conductores.append(nombres_conductores)

    
 

for c in lista_conductores:
    print('------------------------------------')
    print(f'el nombre del conductor es: {c[0]}')
    print(f'los kilometros realizados son: {c[1]}')
    print(f'el total de kilometros recorridos es: {c[2]}')