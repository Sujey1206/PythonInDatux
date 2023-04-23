#EJERCICIO 10
dnis = ['12345678A', '23456789B', '34567890C']
datos = [
    ['Juan', 25, 'SJL', 'Datux', 'Curso: Python'],
    ['Ana', 17, 'Breña', 'Datux', 'Curso: SQL'],
    ['Pedro', 30, 'La Victoria', 'Datux', 'Curso: Python']
]

dni = input("Ingrese su DNI: ")
if dni in dnis:
    indice = dnis.index(dni)
    persona = datos[indice]
    if persona[1] >= 18 and persona[3]=='Datux' and "Python" in persona[4]:
        print("Tiene permitido ingresar al curso de Python.")
    else:
        print("Lo siento, no cumple con los requisitos para ingresar al curso de Python.")
else:
    print("Lo siento, su DNI no está en la lista.")