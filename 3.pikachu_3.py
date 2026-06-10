#Clase encapsulamiento
class Pikachu:
    tipo = 'Electrico' #Atributos de clase
    
    
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):#Inciializador
        self.nombre = nombre #Atributos de instancia
        self.nivel = nivel
        self.salud = salud
        self.voltaje_maximo = voltaje_max
        self.amperaje_maximo = amperaje_max
        self.color = color
        
        self.color = color

    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} de daño")

pikachu_1 = Pikachu('Pepe',780,100,6,2,'Amarillo')


print(f"El pikachu llamado {pikachu_1.nombre} tiene un nivel {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}")