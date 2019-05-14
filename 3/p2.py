numberString = input("Podaj liczbe w systemie o podstawie 2: ")
number = 0


for i in range (0, len(numberString)):
    number = number*2 + int(numberString[i])

print("\nLiczba w syetmie dziesietnym: ")    
print(number)