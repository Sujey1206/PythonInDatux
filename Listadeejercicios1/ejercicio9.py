#EJERCICIO 9
python = []
sql = []
pbi = []
print("""
------------------------------
1. Agrega lista de python
2. Agrega lista de SQL
3. Agregar a lista Power BI
------------------------------
""")
valor = int(input("Ingresa un valor: "))
match valor:
    case 1:
        lista_py = input("Agregar lista de python")
        python.append(lista_py)
        print(python)
    case 2:
        lista_sql = input("Agregar lista de SQL")
        sql.append(lista_sql)
        print(sql)
    case 3:
        lista_pbi = input("Agregar lista de Power BI")
        pbi.append(lista_pbi)
        print(pbi)
    case _:
        print("No ingreso una opcion correcta")
