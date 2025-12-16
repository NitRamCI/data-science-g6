class Persona:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Email: {self.email}')

class Alumno(Persona):
    def __init__(self, nombre, email, curso):
        super().__init__(nombre,email)
        self.curso = curso

    def mostrar(self):
        print('::: Datos del Alumno :::')
        super().mostrar()
        print(f'Curso: {self.curso}')

class Profesor(Persona):
    def __init__(self,nombre,email,especialidad):
        super().__init__(nombre,email)
        self.especialidad = especialidad

    def mostrar_profesor(self):
        print('::: Datos del Profesor :::')
        super().mostrar()
        print(f'Especialidad: {self.especialidad}')

alumno1 = Alumno('Juan Perez', 'juan@gmail.com','fisica')
alumno1.mostrar()

profesor1 = Profesor('Ana Gomez', 'ana@gmail.com', 'Matematicas')
profesor1.mostrar()