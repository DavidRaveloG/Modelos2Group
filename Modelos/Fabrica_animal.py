from Gato import Gato
from Perro import Perro
class Fabrica_A():
    @staticmethod
    def construir(tipo_animal,color_raza,edad,sexo):
        if tipo_animal == 'Gato':
            return Gato(color_raza,edad,sexo)
        elif tipo_animal == 'Perro':
            return Perro(color_raza,edad,sexo)
        else: 
            return None
        
