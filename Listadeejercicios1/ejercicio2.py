#EJERCICIO 2
radio = float(input("Ingresa la medida del radio: "))
base = float(input("Ingresa la medida de la base del triangulo: "))
altura = float(input("Ingresa la medida de la altura del triangulo: "))
lado = float(input("Ingresa la medida del lado del triangulo: "))

area_cir= (radio**2)*3.14
area_tri= (base*altura)/2
area_cua= lado**2

print("""----------------
El area del circulo es: {} m2
El area del triangulo es:  {} m2
El area del cuadrado es:  {} m2
----------------
""".format(area_cir, area_tri, area_cua))