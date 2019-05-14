#SOrtowanie przez wstawianie
import random

random.seed()

N = 5

lista = [0]*N

for i in range (0,N):   lista[i] = random.randrange(100)
    
print (lista)

for j in range (1,N):
    cur = lista[j]
    for i in range (j - 1, -1, -1):
        if lista[i] > cur:
            lista[i+1], lista[i] = lista[i], lista[i+1]
        else:
            break
    
print (lista)