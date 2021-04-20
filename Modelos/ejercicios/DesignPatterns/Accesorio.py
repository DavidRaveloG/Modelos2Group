from AnimalDecorado import AnimalDeco
from IAnimal import Animal

class Acces(AnimalDeco):


    def __init__(self, Animal):
        super().__init__(Animal)
        self.__accesorio = 'saco'

    def accesorioAnimal(self):
        print('El accesorio añadido fue '+self.__accesorio) 

    def saludo(self):
        super().saludo()

    def comida_preferida(self):
        super().comida_preferida()

    def adoptar(self):
        super().adoptar()
