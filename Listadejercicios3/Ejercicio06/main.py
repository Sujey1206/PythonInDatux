from catalogo import Catalogo
from pelicula import Pelicula

if __name__ == "__main__":
    pelicula1=Pelicula("Guardianes de la galaxia",140,2023)
    pelicula2=Pelicula("El rey leon",120,2018)
    c1=Catalogo()
    c1.agregar(pelicula1)
    c1.agregar(pelicula2)
    c1.mostrar()
