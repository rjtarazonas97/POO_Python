from tipoelectrico import TipoElectrico

class Pikachu(TipoElectrico):
    #__tipo = 'Electrico' #Atributos de clase
    
    
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):#Inciializador
        # self.nombre = nombre #Atributos de instancia
        # self.__nivel = nivel
        # self.__salud = salud ya no los necesito poruque heredo de la clase pokemon
        # aca se utiliza KWARG ARGUMENTS por eso se definide cada atributo
        super().__init__(nombre=nombre,
                          nivel=nivel,
                          salud = salud,
                          color = color,
                          amperaje_max= amperaje_max,
                          voltaje_max= voltaje_max)
        self.__voltaje_maximo = voltaje_max #Atributos que no pueden ser modificados se denota con el guion abajo
        self.__amperaje_maximo = amperaje_max# simula el ccomportamiento de privacidad para que el atributo no sea modificado
        #self.color = color
        
        self.color = color

    
    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} de daño")

pikachu_1 = Pikachu('Pepe',780,100,-9000,2,'Amarillo')

pikachu_1.salud = 500


print(f"El pikachu llamado {pikachu_1.nombre} tiene un voltaje maximo de {pikachu_1.voltaje_maximo}")