def primo(x):
    a=0
    pri=0
    
    for z in range(1, x+1):
         if x%z ==0:
             a=a+1
    if a >2:
        pri='false'
    elif a == 1:
        pri='es uno'
    else:
        pri='true'
    print(pri)

    
z=int(input('Ingrse un Número  '))
primo(z)
