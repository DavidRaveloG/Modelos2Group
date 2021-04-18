from IAnimal import Animal

class Perro(Animal):
    def __init__(self,raza,edad,sexo):
        self.raza=raza
        self.edad=edad
        self.sexo=sexo
    def comida_preferida(self):
        print('Su comida preferida es el Chunky')
    def saludo(self):
        print('Tu nuevo perro te saluda: GUAU')
    def adoptar(self):
        print('Información del perro: ')
        print('Raza: '+self.raza)
        print('Edad: '+self.edad+' años')
        print('Sexo: '+self.sexo)
        print('Se adoptado con exito, cuida muy bien de tu nuevo Perro')

    