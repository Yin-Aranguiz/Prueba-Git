def primo(num):
    if num == 1 or num == 0:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
num=0
for z in range (1,355):
    if primo(z)==True:
        num += z
print(num)