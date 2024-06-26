def suma(a,b):
    sum = a + b
    return sum
def resta(a,b):
    res = a - b
    return res
def division(a,b):
    div = a / b
    return div
def multiplicacion(a,b):
    mult = a * b
    return mult
#------------------
cantidadNumeros = int(input('Cantidad de números a operar: '))
lista = []
operadores = []
resultado = 0
for n in range(1,cantidadNumeros+1):
    if n != cantidadNumeros:
        numero = int(input(f'Ingrese el {n}° número: '))
        lista.append(numero)
        operador = input('Ingrese que operación quiere realizar "+" "-" "*" "/": ')
        lista.append(operador)
        while operador != "+" and operador != "-" and operador != "*" and operador != "/":
             operador = input('Ingrese que operación quiere realizar "+" "-" "*" "/": ')
             lista.append(operador)
    else:
        numero = int(input(f'Ingrese el {n}° número: '))
        lista.append(numero)
for n in range(0,len(lista)):
    if lista[n] == '*':
        resultado = multiplicacion(lista[n-1],lista[n+1])
    elif lista[n] == '/':
        resultado = division(lista[n-1],lista[n+1])
    elif lista[n] == '+':
        resultado = suma(lista[n-1],lista[n+1])
    elif lista[n] == '-':
        resultado = resta(lista[n-1],lista[n+1])
#-------------------
print(lista)
print(resultado)