#HERENCIA CLASE PADRE
class Pokemon:
    
    def __init__(self,nombre, nivel, salud, color):
        self.nombre = nombre#constructores
        self.__nivel = None  #clase privada
        self.__salud = None
        self.color = color
        
        #Interfaz segura para la modficacion de instancia
        self.salud = salud
        self.nivel = nivel
        
    @property #estos son decoradores
    def salud(self): #getter
        return self.__salud
    
    @salud.setter #setter
    def salud(self,salud):
        if salud > 0 and salud <= 100:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa",
                  "La salud no puede ser mayor a 100")
            
    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self,nivel):
        if nivel > 0 and nivel <= 1000:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo",
                  "El nivel no puede ser mayor a 1000")       