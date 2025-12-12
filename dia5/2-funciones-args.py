def sumar (a, b):
    return a + b

print(sumar(3, 5))  


#listas arg

def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args
        resultado = resultado + numero
    return resultado

suma1 = sumar_todos(1, 2, 3, 4, 5)
print(suma1)