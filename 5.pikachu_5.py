#Clase encapsulamiento 2
class Pikachu:
    __tipo = 'Electrico' #Atributos de clase
    
    
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):#Inciializador
        self.nombre = nombre #Atributos de instancia
        self.__nivel = nivel
        self.__salud = salud
        self.__voltaje_maximo = voltaje_max #Atributos que no pueden ser modificados se denota con el guion abajo
        self.__voltaje_maximoamperaje_maximo = amperaje_max# simula el ccomportamiento de privacidad para que el atributo no sea modificado
        self.color = color
        
        self.color = color
       
    @property #estos son decoradores
    def salud(self): #getter
        return self.__salud
    
    @salud.setter #setter
    def salud(self,salud):
        if salud > 0 and salud < 5000:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa",
                  "La salud no puede ser mayor a 5000")

    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} de daño")

pikachu_1 = Pikachu('Pepe',780,100,6,2,'Amarillo')

pikachu_1.salud = 500


print(f"El pikachu llamado {pikachu_1.nombre} tiene una salud de {pikachu_1.salud}")