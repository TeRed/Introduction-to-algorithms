import time

def fibo (n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibo(n-1) + fibo(n-2)
    
def fibo2 (n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
        
    a = 0
    b = 1
    c = 0
    
    for i in range (1, n):
        c = a + b
        a = b
        b = c
        
    return c
    

nread = int(input("Podaj fibo: "))

start_time = time.time()
print(fibo(nread))
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
print(fibo2(nread))
print("--- %s seconds ---" % (time.time() - start_time))