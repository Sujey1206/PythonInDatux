import pandas as pd
columnas = ['Nombre', 'Apellido', 'Edad', 'Cursos', 'Celular', 'Correo']
ruta_archivo = 'datos2.csv'
datos = pd.read_csv(ruta_archivo, usecols =columnas, sep=';')

datos_filtrados = datos[datos['Edad'] > 35]

datos2 = pd.DataFrame({'Nombre': ['Josep', 'Esther', 'Laura'], 'Nota': ['18', '10', '16']})
datos_combinados = pd.merge(datos, datos2, on='Nombre')

datos['NuevaColumna'] = ['Valor1', 'Valor2', 'Valor3', 'Valor4', 'Valor5', 'Valor6', 'Valor7', 'Valor8', 'Valor9', 'Valor10']

filtro = datos[datos['Edad'] > 35]
datosmerge = pd.DataFrame({'Nombre': ['Josep', 'Esther', 'Laura'], 'Nota': ['18', '10', '16']})
datos_juntos = pd.merge(filtro, datosmerge, on='Nombre')
datos_juntos['Estado'] = ['Aprobado', 'Desaprobado', 'Aprobado']
print(datos_juntos)
