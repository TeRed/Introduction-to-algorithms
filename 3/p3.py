number = int(input("Podaj liczbe w systemie o podstawie 10: "))
base = int(input("Podaj podstawe systemu: "))

lista = []

while (number > 0):
    rest = number % base
    if(rest > 9):
        lista.append(chr((rest-10) + ord('A')))
    else:
        lista.append(rest)
    number = int(number / base)

lista.reverse()

print(lista)
    
printer = "".join(map(str, lista))

print(printer)