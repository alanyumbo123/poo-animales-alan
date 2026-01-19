# Clase base Animal
# Aplica encapsulación

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    def hacer_sonido(self):
        return "El animal hace un sonido"

    def get_edad(self):
        return self._edad
