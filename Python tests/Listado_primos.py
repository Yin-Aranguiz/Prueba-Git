x = int(input('Ingresa hasta que numero quieres determinar un primo: '))
a=0
pri=0
lista=[]
for v in range(2,x):
    for z in range(2,x):
        if x%z ==0:
            print(x)




'''    
for z in range(1, x+1):
    for c in range(1,x+1):
        if c%z == 0:
            a= a +1
            if a > 2 or a==1:
                a=0
            else:
                print(z)
            
'''           

print(a)
'''
    if x%z == 0:
        a = a + 1
    elif a == 2:
        print(z)
'''    

