menu = int(input('Ingrese "1" para acceder al Menú '))
while menu != 1:
    menu = int(input('Ingrese "1" para acceder al Menú '))
while menu==1:
    x=int(input('1-.Opción 1: \n2-.Opción 2: \n3-.Salir: \n'))
    if x == 1:
        print('Opción 1 \nJugar')
    elif x== 2:
        print('Opción 2 \nComer')
    elif x== 3:
        menu=int(input('Para volver a ingresar presione "1", si no presione cualquier otra tecla para cerrar el programa\n'))
