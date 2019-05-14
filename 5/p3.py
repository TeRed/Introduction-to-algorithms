high = int(input("Podaj wysokosc trojkata: "))

def pas(x, y):
    if(x == y or y == 1):
        return 1
    return pas(x - 1, y) + pas(x - 1, y - 1)

if(high >= 1):
    print("1")

for i in range (2, high+1):
    print("1 ", end="")
    for j in range (2, i):
        print(pas(i, j), end="")
        print(" ", end="")
    print("1")