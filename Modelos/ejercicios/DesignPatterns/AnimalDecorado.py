from IAnimal import Animal

class AnimalDeco(Animal):
  
    def __init__(self, Animal):
        self.__animal = Animal

    def accesorioAnimal():
        pass

    def saludo(self):
        self.__animal.saludo()

    def comida_preferida(self):
        self.__animal.comida_preferida()

    def adoptar(self):
        self.__animal.adoptar()

    




