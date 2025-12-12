# funciones en python
# una función es un bloque de código reutilizable que realiza una tarea específica
# se define usando la palabra clave 'def' seguida del nombre de la función y paréntesis

def saludar(nombre):
    mensaje = f'hola {nombre}'
    return mensaje

# llamando a la función
usuario = input(' como te llamas?? ')
print(saludar(usuario))
