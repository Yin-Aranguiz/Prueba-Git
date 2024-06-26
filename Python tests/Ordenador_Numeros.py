cantidadNum = int(input('Cuantos números vas a ingresar: '))
lista = []
for n in range(1,cantidadNum+1):
    number = int(input('Ingrese el numero:'))
    lista.append(number)
lista.sort()
print(f'El número mayor es: {lista[cantidadNum-1]}, el menor es {lista[0]}')
print('----------------------------')
print(f'Los números son {lista}')