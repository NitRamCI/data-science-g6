# PROGRAMACION ORIENTADA A OBJETOS (POO)
# LAS CLASES SON PLANTILLAS PARA CREAR OBJETOS
# UNA CLASE PUEDE CONTENER ATRIBUTOS (VARIABLES) Y METODOS (FUNCIONES)
class Automovil:
    def __init__(self,aa,pl,col,mar):
        self.año=aa
        self.placa=pl
        self.color=col
        self.marca=mar
    def encender(self):
        print(f'Encender el automovil {self.marca}')

    def avanzar(self):
        print(f'Avanzar el automovil {self.marca}')

    def acelerar(self):
        print(f'Acelerar el automovil {self.marca}')

    def frenar(self):
        print(f'Frenar el automovil {self.marca}')

# CREAR OBJETOS A PARTIR DE LA CLASE
vw=Automovil(2020,'ABC123','Rojo','Volkswagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(2018,'XYZ789','Azul','tico')
tico.encender()
tico.avanzar()  
tico.acelerar()
tico.frenar()



