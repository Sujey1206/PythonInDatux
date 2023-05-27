import re

def validar_entrada(expresion_regular, entrada):
    patron = re.compile(expresion_regular)
    return re.match(patron, entrada) is not None

print("-------------------------------------\n")
entrada = input("Ingrese una entrada: ")
print("\n-------------------------------------")
if validar_entrada(r'^\d+$', entrada):
    print('La entrada es numérica VALIDA')
else:
    print('La entrada es numérica INVALIDA')

# Validar para texto
if validar_entrada(r'^[a-zA-Z\s]+$', entrada):
    print('La entrada de texto es VALIDA')
else:
    print('La entrada de texto es INVALIDA')

# Validar para dirección de correo electrónico
if validar_entrada(r'^[\w\.-]+@[\w\.-]+\.\w+$', entrada):
    print('La dirección de correo es VALIDA')
else:
    print('La dirección de es INVALIDA')

# Validar para número de teléfono
if validar_entrada(r'^\+?51\d{9}$', entrada):
    print('El número de teléfono es VALIDA')
else:
    print('El número de teléfono es INVALIDA')
