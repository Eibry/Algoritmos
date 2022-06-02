menu = """
Programa para realizar operaciones aritméticas

Elige una operación aritmética

1- suma
2- Resta
3- Multiplicación
4- División
5- Residuo
6- División Entera
7- Exponentes
8- Raices

Ingresa el número de la opción
"""

option = int(input(menu))

def message(operacion, menu):
    if menu < 7:
        print("Elegiste " + operacion)
        number1 = float(input("Dame un numero "))
        number2 = float(input("Dame otro numero "))
        result(menu, number1, number2)
    else:
        print("Elegiste " + operacion)
        number1 = float(input("Dame un numero "))
        result(menu, number1,0)
        

def result(menu, number1, number2):
    if menu == 1:
        result = number1 + number2
    elif menu == 2:
        result = number1 - number2
    elif menu == 3:
        result = number1 * number2
    elif menu == 4:
        result = number1 / number2
    elif menu == 5:
        result = number1 % number2
    elif menu == 6:
        result = number1 // number2
    elif menu == 7:
        result = number1 ** 2
    elif menu == 8:
        result = number1 ** 0.5
    print("El resultado es: "+ str(result))

if option == 1:
    message("La suma",1)
elif option == 2:
    message("La resta",2)
elif option == 3:
    message("La multiplicación",3)
elif option == 4:
    message("La división",4)
elif option == 5:
    message("El residuo",5)
elif option == 6:
    message("La división entera",6)
elif option == 7:
    message("El cuadrado",7)
elif option == 8:
    message("La raíz cuadrada",8)
else:
    print("El número es invalido 😒")
