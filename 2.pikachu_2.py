#Clase
class Pikachu:
    tipo = 'Electrico' #Atributos de clase
    
    
    def __init__(self, nombre, nivel, salud):#Inciializador
        self.nombre = nombre #Atributos de instancia
        self.nivel = nivel
        self.salud = salud
        
    def atacar(self): #m3.etodos
        print(f"Pikachu ataca y genera {self.nivel/4}")

pikachu_1 = Pikachu('Jesus', 800, 1000)
pikachu_2 = Pikachu('Juan', 1200, 1002)

print(f"El Pikachu llamado {pikachu_1.nombre} ataca.")
pikachu_1.atacar()

print(f"El Pikachu llamado {pikachu_2.nombre} ataca.")
pikachu_2.atacar()