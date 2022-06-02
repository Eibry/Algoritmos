number = int(input("Dame un número "))
if number >= 1:
    print("El número " + str(number) + " es positivo")
elif number < 0:
    print("El número " + str(number) + " es negativo")
else:
    print("El número " + str(number) + " es nulo")