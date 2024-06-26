#1-Muestra si el número es par o impar

for n in range(1,11):
    if n%2==0:
        print(str(n)+' - es par')
    else:
        print(str(n)+' - es impar')
print('\n')

#2-Suma de los 10 primeros numeros naturales
x=1
y=0
for x in range(1,11):
    y+=x
print(y)
print('\n')

#3-Tabla del 5
numero=0
for numero in range(1,13):
    multiplicado=numero*5
    print('5x'+str(numero)+' = '+str(multiplicado))    

#4-Contador de letras a
palabra=input('Escriba una palabra: ')
i=0
for a in palabra:
    if a=='a' or a=='A':
        i=i+1
print('La palabra tiene '+str(i)+' letras a')


#5-Encontrar numero mayor de una lista dada
lista=[1,2,3,4,100,5,6,10]
mayor=0
for num in lista:
    if num > mayor:
        mayor = num
print(mayor)


#6-Números divisibles por 3
for n in range(1,31):
    if n%3==0:
        print(str(n)+ ' es multiplo de 3')
print('\n')

#7-Contador de números + y -
i3=0
i4=0
lista_enteros = [-1,5,-2,-3,4]
for n in lista_enteros:
    if n >= 0:
        i3=i3+1
    else:
        i4=i4+1
print('Hay '+str(i3)+' Números positivos y hay '+str(i4)+' Números negativos')

