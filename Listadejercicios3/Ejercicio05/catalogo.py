class Producto:
    def __init__(self, nom, cod, precio):
        self.nom = nom
        self.cod = cod
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(f"{producto.nom} ({producto.cod}): ${producto.precio}")
