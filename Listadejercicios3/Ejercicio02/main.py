from catalogo import Catalogo, Producto

if __name__ == "__main__":
    catalogo = Catalogo()
    catalogo.agregar(Producto("Bateria", "BT01", 2500))
    catalogo.agregar(Producto("Frenos", "FR01", 500))
    catalogo.agregar(Producto("Llanta", "LT01", 800))
    catalogo.mostrar()
