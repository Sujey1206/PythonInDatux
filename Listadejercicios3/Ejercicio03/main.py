def dividir(num1, num2):
   if num2!=0:
      resultado = num1 / num2
      return resultado 
   else:
       print("No se puede dividir entre cero.")
        

if __name__ == "__main__":
    opcion = ""
    while opcion != "2":
        print("---------MENU---------\n")
        print("1. Dividir dos números")
        print("2. Salir")
        print("----------------------\n")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = dividir(num1, num2)
            if resultado is not None:
                print(f"El resultado de la división es: {resultado}")
        elif opcion != "2":
            print("Opción no válida.")
