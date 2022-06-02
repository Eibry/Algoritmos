number = int(input("Ingresa un número "))

if number > 20:
    sobra = number - 20
    print("Sobran " + str(sobra))
elif number < 20:
    falta = 20 - number
    print("Faltan " + str(falta))
else:
    print("Tu número es 20")