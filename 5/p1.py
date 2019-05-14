import time

def silnia (n):
    if (n == 1):
        return 1
    return n*silnia(n-1)
    
def silnia2 (n):
    result = 1
    for i in range (1, n+1):
        result = result * i
        
    return result

nread = int(input("Podaj silnie: "))

start_time = time.time()
print(silnia(nread))
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
print(silnia2(nread))
print("--- %s seconds ---" % (time.time() - start_time))