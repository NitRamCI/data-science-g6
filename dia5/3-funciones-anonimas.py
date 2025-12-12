# funciones anonimas (lambdas)
# las funciones anonimas son funciones que no tienen un nombre asociado
# se definen usando la palabra clave 'lambda' seguida de los parámetros, dos puntos y

def sumar(a, b):
    return a + b

sumar2 = lambda a, b: a + b

print(sumar2(10, 15))
print(sumar(10, 15))
