import random
import time
random.seed()

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

lista = [-1]*b

losowana = random.randrange(a)

while True:
    for i in range (b-1,-1,-1):
        if(i > 0):        
            lista[i] = lista[i-1]
        else:
            lista[i] = -1
            
    lista[0] = random.randrange(a)
    
    for x  in range (0,b):
        for i in range (0,a):
            if(lista[x] == i):
                print('X', end="")
            else:
                print('0', end="")
        print("")
    
    for x in range (0,25):
        print("")
    time.sleep(0.3)