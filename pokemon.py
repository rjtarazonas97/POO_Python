#HERENCIA CLASE PADRE
class Pokemon:
    
    def __init__(self,nombre, nivel, salud, color):
        self.nombre = nombre#constructores
        self.__nivel = nivel #clase privada
        self.__salud = salud
        self.__color = color
        
        