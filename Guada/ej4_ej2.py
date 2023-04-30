# Ej2
print('Hello python')

def validarNum(numero):
    numero_str = str(numero)
    if(type(numero) == int) and (len(numero_str) == 2):
        return True
    else:
        return False
       

list_num = []

bandera = False

while bandera == False:
    num = int(input('Ingresar numero: '))
   
    if(num == 0) or (validarNum(num) == False):
        bandera = True
    else:
        list_num.append(num)

promedio = 0

for i in list_num:
    promedio += i

promedio = promedio / len(list_num)

print(promedio)