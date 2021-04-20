from IAnimal import Animal

class Gato(Animal):
    def __init__(self,color,edad,sexo):
        self.color=color
        self.edad=edad
        self.sexo=sexo
    def comida_preferida(self):
        print('Su comida preferida son los Whiskas')
    def saludo(self):
        print('Tu nuevo gato te saluda: MIAU')
    def adoptar(self):
        print('Información del gato: ')
        print('Color: '+self.color)
        print('Edad: '+self.edad+' años')
        print('Sexo: '+self.sexo)
        print('Se adoptado con exito, cuida muy bien de tu nuevo Gato')


    