def main():
    datos = guardar_datos()
    imprimir_datos(datos)
    verificacion = verificar(datos)
    print(verificacion)

def guardar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dni = input("Ingrese su DNI: ")
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "dni": dni
    }
    return datos

def imprimir_datos(datos):
    print("\nDatos del usuario:")
    print("Nombre:", datos["nombre"])
    print("Apellido:", datos["apellido"])
    print("Edad:", datos["edad"])
    print("DNI:", datos["dni"])

def verificar(datos):
    if "" in datos.values():
        mensaje= "\nAcceso denegado por falta de datos.\n"
    else:
        edad = int(datos["edad"])
        if edad >=18:
            mensaje = "\nBienvenido al sistema!\n"
        else:
            mensaje = "\nAcceso denegado por minoria de edad.\n"
    return mensaje
main()