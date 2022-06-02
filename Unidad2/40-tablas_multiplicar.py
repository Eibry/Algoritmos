number = int(input("¿Cuál tabla te gustaría conocer? "))

for i in range(1,11):
    result = number * i
    print(str(number) + " x " + str(i) + " = " + str(result))