def obtener_primos_en_rango(maximo, step):
    no_primos = [False] * (maximo + 1)
    no_primos[0] = True
    no_primos[1] = True
    for numero in range(2, maximo + 1, step):
        if not no_primos[numero]:
            lista_primos.append(numero)
            for i in range(numero * 2, maximo + 1, numero):
                no_primos[i] = True
    return lista_primos

lista_primos = []
maximo = 10**5
step = 5
lista_primos = obtener_primos_en_rango(maximo, step)
print(lista_primos)