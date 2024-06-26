edad=int(input('Ingresa tu edad'))

if edad >= 18:
    print('es mayor de edad')
elif edad <= 18:
    print('es menor de edad')

Numero=1
'''for numero in range(1,101):
    if numero % 15 == 0:
        print('FizzBuzz '+ str(numero))
    elif numero % 3 == 0 and numero != 55 and numero != 24:
        print('Fizz '+ str(numero))
    elif numero % 5 == 0 and numero != 55 and numero != 24:
        print('Buzz '+ str(numero))
    elif numero == 24 or numero== 55:
        print(str(numero))
    else:
        print(numero)
'''