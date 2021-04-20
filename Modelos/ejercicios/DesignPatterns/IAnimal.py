from abc import ABC, abstractstaticmethod


class Animal(ABC):
 
    def __init__(self,color_raza,edad,sexo):
        self.color_raza=None
        self.edad=None
        self.sexo=None

    @abstractstaticmethod
    def saludo(self):
        pass

    @abstractstaticmethod
    def comida_preferida(self):
        pass

    @abstractstaticmethod
    def adoptar(self):
        pass
