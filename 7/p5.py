#Babelkowe
import random

random.seed()

N = 5

lista = [0]*N

for i in range (0,N):   lista[i] = random.randrange(100)
    
print (lista)

for j in range (0,N - 1):
    for i in range (0,N - j - 1):
        if (lista[i] > lista[i+1]):
            lista[i+1], lista[i] = lista[i], lista[i+1]

print (lista)