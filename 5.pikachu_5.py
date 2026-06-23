#Clase encapsulamiento 2
from pokemon import Pokemon
class Pikachu(Pokemon):
    __tipo = 'Electrico' #Atributos de clase
    
    
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):#Inciializador
        # self.nombre = nombre #Atributos de instancia
        # self.__nivel = nivel
        # self.__salud = salud ya no los necesito poruque heredo de la clase pokemon
        super().__init__(nombre=nombre,nivel=nivel,salud = salud, color = color)
        self.__voltaje_maximo = voltaje_max #Atributos que no pueden ser modificados se denota con el guion abajo
        self.__amperaje_maximo = amperaje_max# simula el ccomportamiento de privacidad para que el atributo no sea modificado
        #self.color = color
        
        self.color = color
       
    @property #estos son decoradores
    def salud(self): #getter
        return self._Pokemon__salud
    
    @salud.setter #setter
    def salud(self,salud):
        if salud > 0 and salud < 5000:
            self._Pokemon__salud = salud
        else:
            print("La salud no puede ser negativa",
                  "La salud no puede ser mayor a 5000")
            
    @property
    def nivel(self):
        return self._Pokemon__nivel
    
    @nivel.setter
    def nivel(self,nivel):
        if nivel > 0 and nivel <= 1000:
            self._Pokemon__nivel = nivel
        else:
            print("El nivel no puede ser negativo",
                  "El nivel no puede ser mayor a 1000")

    @property
    def voltaje_maximo(self):
        return self._Pokemon__voltaje_maximo
    
    @voltaje_maximo.setter
    def voltaje_maximo(self,voltaje_maximo):
        if voltaje_maximo > 0:
            self._Pokemon__voltaje_maximo = voltaje_maximo
        else:
            print("El valor no puede ser negativo")
    
    @property
    def amperaje_maximo(self):
        return self._Pokemon__amperaje_maximo
    
    @amperaje_maximo.setter
    def amperaje_maximo(self,amperaje_maximo):
        if amperaje_maximo > 0:
            self._Pokemon__amperaje_maximo = amperaje_maximo
        else:
            print("El amperaje no puede ser negativo")
    
    
    def atacar(self):
        print(f"Pikachu ataca y genera {self._Pokemon__nivel/4} de daño")

pikachu_1 = Pikachu('Pepe',780,100,6,2,'Amarillo')

pikachu_1.salud = 500


print(f"El pikachu llamado {pikachu_1.nombre} tiene una salud de {pikachu_1.salud}")