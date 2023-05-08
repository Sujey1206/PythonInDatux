class Catalogo:
    listaPeliculas=[]
    def __init__(self) -> None:
        self.name="Catalogo Peliculas"
        self.listaPeliculas=[]
    def agregar(self, x):
        self.listaPeliculas.append(x)
    def mostrar(self):
        for iterador in self.listaPeliculas:
            print(iterador) 
    def filtroDuracion(self,duracion=0):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.duracion>duracion:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro
