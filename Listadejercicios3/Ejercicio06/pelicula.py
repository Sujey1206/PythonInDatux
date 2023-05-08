class Pelicula:
    def __init__(self,nombre,duracion,release) -> None:
        self.nombre=nombre
        self.duracion=duracion
        self.release=release
    def __str__(self) -> str:
        return f"{self.nombre} se estreno el {self.release} y dura {self.duracion} minutos"
