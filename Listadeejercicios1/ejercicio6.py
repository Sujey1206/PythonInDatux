#EJERCICIO 6
n = int(input("Ingrese un valor límite: "))
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma de los números hasta el valor ingresado es: {suma}")