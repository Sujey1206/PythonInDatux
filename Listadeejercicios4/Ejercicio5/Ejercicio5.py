import pandas as pd
import sqlite3

columnas = ['Nombre', 'Apellido', 'Edad', 'Cursos', 'Celular', 'Correo']
ruta_archivo = 'datos2.csv'
datos = pd.read_csv(ruta_archivo, usecols=columnas, sep=';')

filtro = datos[datos['Edad'] > 35]
datosmerge = pd.DataFrame({'Nombre': ['Josep', 'Esther', 'Laura'], 'Nota': ['18', '10', '16']})
datos_juntos = pd.merge(filtro, datosmerge, on='Nombre')
datos_juntos['Estado'] = ['Aprobado', 'Desaprobado', 'Aprobado']
print(datos_juntos)

conexion = sqlite3.connect('data_alumnos.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
    nombre TEXT,
    apellido TEXT,
    edad INTEGER,
    cursos TEXT,
    celular TEXT,
    correo TEXT,
    nota TEXT,
    estado TEXT
)''')

for _, row in datos_juntos.iterrows():
    cursor.execute('''INSERT INTO alumnos (nombre, apellido, edad, cursos, celular, correo, nota, estado)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (row['Nombre'], row['Apellido'], row['Edad'], row['Cursos'], row['Celular'],
                    row['Correo'], row['Nota'], row['Estado']))


conexion.commit()
conexion.close()

print("Los datos se han registrado en la base de datos.")
