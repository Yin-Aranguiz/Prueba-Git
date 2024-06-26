palabraTest = input('Ingrese palabra para comprobar si es palindromo: ')
length = len(palabraTest)
par = True
if length % 2 == 0:
    par = True
else:
    par = False
if par == True:
    for n in range(1, length+1):
        palabraTest[n]

def primo(a,y):
    return (a+1)-(y+4)
print(primo(5,6))