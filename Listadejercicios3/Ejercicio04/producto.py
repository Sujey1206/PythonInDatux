class Producto:
    def __init__(self, nomb, cod):
        self.nomb = nomb
        self.cod = cod

    def __str__(self):
        pais, lote, anio = self.cod.split("-")
        return f"Nombre: {self.nomb}\nCodigo: {self.cod}\nPaís de origen: {pais}\nNúmero de lote: {lote}"
