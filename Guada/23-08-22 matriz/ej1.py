### Ej 1
## 5 equipos
matriz = [                  # eq1 eq2 eq3 eq4 eq5
    [0, 3, 1, 2, 1], # eq 1
    [1, 0, 3, 2, 3], # eq 2
    [0, 2, 0, 1, 1], # eq 3
    [1, 0, 2, 0, 1], # eq 4
    [3, 4, 1, 2, 0]  # eq 5
]

#print(goles) # muestra todo

# muestra cada equipo separado por ---
count = 0
for row in matriz:
    print('fila', count)
    print(row)
    count +=1

equipos = [
    { 'eq1': 0 },
    { 'eq2': 0 },
    { 'eq3': 0 },
    { 'eq4': 0 },
    { 'eq5': 0 }
]

