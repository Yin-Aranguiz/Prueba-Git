def calcular_expresion(expresion):
    try:
        resultado = eval(expresion)
        return f"El resultado de '{expresion}' es: {resultado}"
    except Exception as e:
        return f"Error: {str(e)}"

expresion = input("Ingrese la expresión matemática: ")
print(calcular_expresion(expresion))


print(range(3,100))