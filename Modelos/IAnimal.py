from abc import ABC, abstractstaticmethod

class Animal(ABC):
    @abstractstaticmethod
    def __init__(self,color_raza,edad,sexo):
        self.color_raza=None
        self.edad=None
        self.sexo=None
        
    @abstractstaticmethod
    def saludo():
        pass
    @abstractstaticmethod
    def comida_preferida():
        pass
    @abstractstaticmethod
    def adoptar():
        pass
