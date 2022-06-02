calif_1 = float(input("Primer periodo "))
calif_2 = float(input("Segundo periodo "))
calif_3 = float(input("Tercer periodo "))

prom = (calif_1+calif_2+calif_3)/3

print("Tu calificación final es:"+ str(prom))

if prom > 9 and prom <= 10:
    print("Sobresaliente")
elif prom > 8 and prom <= 9:
    print("Destacado")
elif prom > 7 and prom <= 8:
    print("Satisfactorio")
elif prom <= 7:
    print("No acredita")