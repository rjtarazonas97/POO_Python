from pokemon import Pokemon

class Charmander(Pokemon):
    # aca utilizamos positional arguments por eso todo sale segun su posivion de la clase padre
    def __init__(self, nombre, nivel, salud, color):
        super().__init__(nombre, nivel, salud, color)
        
Charmander_1 = Charmander('chari',500,100,'Rojo')
print(Charmander_1.salud)