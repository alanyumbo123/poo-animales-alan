# Clase derivada Perro
# Herencia y polimorfismo

from modelos.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "El perro ladra"
