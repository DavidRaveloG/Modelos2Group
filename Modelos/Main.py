from IAnimal import Animal
from Fabrica_animal import Fabrica_A
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
    elif opcion == 2:
        print('Ha escogido un Perro')
        raza=input('Que raza desea que tenga el Perro: ')
        edad=input('Ingrese la edad que desea que tenga el Perro: ')
        sexo=input('¿Desea que sea macho o hembra?: ')
        Animal=Fabrica_A.construir('Perro',raza,edad,sexo)
    
    Animal.adoptar()
    Animal.saludo()
    Animal.comida_preferida()

if __name__ == '__main__':
    print('Bienvenido al menu de busqueda de animales para adopcion')
    print('Por favor seleccione que tipo de animal desea adoptar')
    menu_Adopcion()
    