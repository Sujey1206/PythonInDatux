import sqlite3
nombre_bd = 'data_alumnos.db'

def leer_datos_alumnos():
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()

    consulta = 'SELECT * FROM alumnos'
    cursor.execute(consulta)

    datos = cursor.fetchall()

    for dato in datos:
        nombre = dato[0]
        apellido = dato[1]
        edad = dato[2]
        cursos = dato[3]
        celular = dato[4]
        correo = dato[5]
        nota = dato[6]
        estado = dato[7]

        print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Cursos: {cursos}, Celular: {celular}, Correo: {correo}, Nota: {nota}, Estado: {estado}")
    conexion.close()
leer_datos_alumnos()
