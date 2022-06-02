num1 = int(input("Escribe el primer número "))
num2 = int(input("Escribe el segundo número "))
num3 = int(input("Escribe el tercer número "))

if num1 == num2 and num1 == num3:
    print("Tus 3 números son iguales")
elif num1 == num2 and num1 > num3:
    print(str(num1) + " es igual a " + str(num2) + " y mayores que " + str(num3))
elif num1 == num2 and num1 < num3:
    print(str(num1) + " es igual a " + str(num2) + " y menores que " + str(num3))
elif num1 == num3 and num1 < num2:
    print(str(num1) + " es igual a " + str(num3) + " y menores que " + str(num2))
elif num1 == num3 and num1 > num2:
    print(str(num1) + " es igual a " + str(num3) + " y mayores que " + str(num2))
elif num1 > num2 and num1 > num3 and num2 > num3:
    print(str(num1) + " es mayor que " + str(num2) + " que es mayor que " + str(num3))
elif num1 < num2 and num1 < num3 and num2 < num3:
    print(str(num3) + " es mayor que " + str(num2) + " que es mayor que " + str(num1))

if number > 10 and number < 20: