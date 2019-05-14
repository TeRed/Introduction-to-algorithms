#Sortowanie przez wybieranie
import random

random.seed()

N = 5

lista = [0]*N

for i in range (0,N):   lista[i] = random.randrange(100)
    
print (lista)

for j in range (0,N - 1):
    min_index = j
    for i in range (j + 1,N):
        if (lista[i] < lista[min_index]):
            min_index = i
    
    lista[j], lista[min_index] = lista[min_index], lista[j]
    
print (lista)