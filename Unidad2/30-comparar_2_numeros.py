num1 = int(input("Escribe el primer número "))
num2 = int(input("Escribe el segundo número "))

if num1 == num2:
    print("Tus números son iguales")
elif num1 > num2:
    print(str(num1) + " es mayor que " + str(num2))
elif num1 < num2:
    print(str(num2) + " es mayor que " + str(num1))