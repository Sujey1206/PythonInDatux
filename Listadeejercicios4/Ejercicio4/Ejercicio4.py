import pandas as pd
columnas = ['Nombre', 'Apellido', 'Edad', 'Cursos', 'Celular', 'Correo']
ruta_archivo = 'datos2.csv'
datos = pd.read_csv(ruta_archivo, usecols =columnas, sep=';')
print(datos)
