#EJERCICIO 3
n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))
n3 = int(input("Ingresa el tercer valor: "))
suma = n1 + n2 + n3
resta = n1 - n2 - n3
multi = n1 * n2 * n3
division = n1 / n2 / n3
entera = (n1%n2)%n3
print(f"""
La suma es: {suma}
La resta es: {resta}
La multiplicacion es: {multi}
La division es: {division}
La division entera es:{entera}
""")