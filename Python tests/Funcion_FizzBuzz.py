def FizzBuzz(numero):
    for numero in range(1,numero):
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

x=int(input('Ingrese numero  '))
FizzBuzz(x)