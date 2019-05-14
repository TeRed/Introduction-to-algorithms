numberString = input("Podaj liczbe: ")
base = int(input("Podaj podstawe systemu: "))
base2 = int(input("Podaj podstawe systemu na jaki ma byc zamienione: "))

number = 0
x = 0

for i in range (0, len(numberString)):
    if (numberString[i].isalpha()):
        x = ord(numberString[i]) - 55
    else:
        x = int(numberString[i])
    number = number*base + x

print (number)    

lista = []

while (number > 0):
    rest = number % base2
    if(rest > 9):
        lista.append(chr((rest-10) + ord('A')))
    else:
        lista.append(rest)
    number = int(number / base2)

lista.reverse()

print(lista)
    
printer = "".join(map(str, lista))

print(printer)