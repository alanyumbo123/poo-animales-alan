# Lógica del sistema

from modelos.perro import Perro

def mostrar_info_animal():
    perro = Perro("Firulais", 3, "Labrador")

    print("Nombre:", perro.nombre)
    print("Edad:", perro.get_edad())
    print("Raza:", perro.raza)
    print("Sonido:", perro.hacer_sonido())
