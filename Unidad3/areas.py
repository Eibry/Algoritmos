menu = """
Programa para calcular áreas

Elige una figura geométrica

1- Cuadrado
2- Rectángulo
3- Triángulo
4- Círculo
5- Pentágono

Escribe el número de la opción
"""

def result(indice, base, height, radio):
    if indice == 1:
        area = base * base
    elif indice == 2:
        area = base * height
    elif indice == 3:
        area = base * height / 2
    elif indice == 4:
        area = 3.1416 * (radio**2)
    elif indice == 5:
        pass    
    print("El área es: " + str(area))

def message(figura):
    print("Elegiste el " + figura)

option = int(input(menu))

if option == 1:
    message("cuadrado")
    base = int(input("¿Cuánto mide uno de los lados? "))
    result(1, base, 0, 0)
elif option == 2:
    message("rectángulo")
    base = int(input("¿Cuánto mide la base? "))
    height = int(input("¿Cuánto mide la altura? "))
    result(2, base, height, 0) 
elif option == 3:
    message("triángulo")
    base = int(input("¿Cuánto mide la base? "))
    height = int(input("¿Cuánto mide la altura? "))
    result(3, base, height, 0) 
elif option == 4:
    message("círculo")
    radio = int(input("¿Cuánto mide el radio? "))
    result(4, 0, 0, radio)
elif option == 5:
    message("pentágono")

else:
    print("El número es invalido")