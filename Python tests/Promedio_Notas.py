import random
cantidadNotas = int(input('Ingrese cantidad de notas: '))
notas = []
promedio = 0
for n in range(1,cantidadNotas+1):
    randomNumber = random.randint(1,7)
    notas.append(randomNumber)
    print(randomNumber)
for n in notas:
    promedio += n

a = promedio/len(notas)

print('El promedio es ' + str(a))
