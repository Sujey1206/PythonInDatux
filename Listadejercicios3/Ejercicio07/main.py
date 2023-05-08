class Persona:
    def __init__(self):
        self.dni = input("Ingrese su DNI: ")
        self.nombre = input("Ingrese sus nombres: ")
        self.apellidos = input("Ingrese sus apellidos: ")
        self.edad = int(input("Ingrese su edad: "))

    def __str__(self):
        return f"DNI:{self.dni} \nNombres: {self.nombre}\nApellidos: {self.apellidos} \nEdad: {self.edad}"
    

if __name__ == "__main__":
    persona = Persona()
    print("-------------------------\n")
    print("DATOS INGRESADOS\n")
    print(persona)  
