biblioteca = {
    "novelas": [
        {"nombre": "Origen", "autor": "Dan Brown", "prestado": False},
        {"nombre": "La madre", "autor": "Máximo Gorki", "prestado": True},
        {"nombre": "Papa Goriot", "autor": "Honoré de Balzac", "prestado": False}
    ],
    "Ciencia": [
        {"nombre": "biologia", "autor": "Jesica Rojas", "prestado": False},
        {"nombre": "quimica", "autor": "Julian Torres", "prestado": False}
    ]
}

usuarios = ["Luis"]

def agregar_usuario(nombre):
    usuarios.append(nombre)

def categorias(biblioteca):
    return list(biblioteca.keys())

def autor_libro(biblioteca):
    libros=[]
    for categoria in biblioteca:
        for libro in biblioteca[categoria]:
            libros.append((libro['nombre'],libro['autor']))
    print(libros)

autor_libro(biblioteca)

usuario_nuevo = "Juan"
agregar_usuario(usuario_nuevo)
print("Usuarios de la biblioteca:")
print(usuarios)