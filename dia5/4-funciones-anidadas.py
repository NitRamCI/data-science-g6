#funciones anidadas
# las funciones anidadas son funciones definidas dentro de otra función
# permiten organizar el código y limitar el alcance de las funciones internas

def operacion (a, b):
    def sumar(x, y):
        return x + y

    def restar(x, y):
        return x - y
    
    print("suma  : ", sumar(a, b))
    print("resta : ", restar(a, b))

operacion(10, 5)

