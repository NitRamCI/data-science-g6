def sumar (a, b):
    return a + b

print(sumar(3, 5))  


#listas arg

def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

suma1 = sumar_todos(1, 2, 3, 4, 5)
print(suma1)

# kwargs

def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'sumar':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'restar':
        return kwargs['a'] - kwargs['b']
    else:
        return 'operacion no soportada'
    

resultado1 = calculadora(operacion='sumar', a=10, b=5)














