import os

def listar_elementos(path):
    elementos = os.listdir(path)
    for elemento in elementos:
        if os.path.isdir(os.path.join(path, elemento)):
            print("Subcarpeta:", os.path.join(path, elemento))
            listar_elementos(os.path.join(path, elemento))

        else:
            print("Archivo:", os.path.join(path, elemento))