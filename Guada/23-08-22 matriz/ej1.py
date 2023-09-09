### Ej 1
## 5 equipos
goles = [                  # eq1 eq2 eq3 eq4 eq5
    [0, 3, 1, 2, 1], # eq 1
    [1, 0, 3, 2, 3], # eq 2
    [0, 2, 0, 1, 1], # eq 3
    [1, 0, 2, 0, 1], # eq 4
    [3, 4, 1, 2, 0]  # eq 5
]

#print(goles) # muestra todo

equipos = [
    { 'eq1': 0 },
    { 'eq2': 0 },
    { 'eq3': 0 },
    { 'eq4': 0 },
    { 'eq5': 0 }
]

# muestra cada equipo separado por ---
cont = 0
for fila in range(len(goles)):
    #print('fila', fila) # muestra el num de fila
    for col in range(len(goles[0])):
        #print('col', col) # muestra num de columna
        #print(goles[fila][col]) 
        if(fila == cont and col == cont):
            #print(cont)
            goles[fila][col] = 1
    cont += 1
    



