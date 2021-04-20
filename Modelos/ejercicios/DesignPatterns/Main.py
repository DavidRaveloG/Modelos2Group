from IAnimal import Animal
from Fabrica_animal import Fabrica_A
from Accesorio import Acces
def menu_Adopcion():
   
    print('1. Gato')
    print('2. Perro')
    opcion = int(input('Seleccione: '))
    if opcion == 1:
        print('Ha escogido un gato')
        color=input('Que color desea que tenga el gato: ')
        edad=input('Ingrese la edad que desea que tenga el gato: ')
        sexo=input('¿Desea que sea macho o hembra?: ')
        Animal=Fabrica_A.construir('Gato',color,edad,sexo)
        accesorio=input('¿Desea incluir un saco como accesorio?')
        if(accesorio == 'si'):
            animalSaco = Acces(Animal) 
            animalSaco.accesorioAnimal()
            animalSaco.adoptar()
            animalSaco.saludo()
            animalSaco.comida_preferida()
        else: 
            Animal.adoptar()
            Animal.saludo()
            Animal.comida_preferida()

    elif opcion == 2:
        print('Ha escogido un Perro')
        raza=input('Que raza desea que tenga el Perro: ')
        edad=input('Ingrese la edad que desea que tenga el Perro: ')
        sexo=input('¿Desea que sea macho o hembra?: ')
        Animal=Fabrica_A.construir('Perro',raza,edad,sexo) 
        accesorio=input('¿Desea incluir un saco como accesorio?')
        if(accesorio == 'si'):
            animalSaco = Acces(Animal) 
            animalSaco.accesorioAnimal()
            animalSaco.adoptar()
            animalSaco.saludo()
            animalSaco.comida_preferida()
        else: 
            Animal.adoptar()
            Animal.saludo()
            Animal.comida_preferida()

if __name__ == '__main__':
    print('Bienvenido al menu de busqueda de animales para adopcion')
    print('Por favor seleccione que tipo de animal desea adoptar')
    menu_Adopcion()
    
