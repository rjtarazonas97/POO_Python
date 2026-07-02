from pokemon import Pokemon

class TipoElectrico(Pokemon):
    
    __tipo = 'Electrico'
    
    def __init__(self,nombre, nivel, salud, voltaje_max, amperaje_max, color):
        super().__init__(nombre = nombre,
                       nivel = nivel,
                       salud = salud,
                       color = color)
        self.__voltaje_maximo = None 
        self.__amperaje_maximo = None
        
        self.voltaje_maximo = voltaje_max
        self.amperaje_maximo = amperaje_max
        
    @property
    def voltaje_maximo(self):
        return self.__voltaje_maximo
    
    @voltaje_maximo.setter
    def voltaje_maximo(self,voltaje_maximo):
        if voltaje_maximo > 0:
            self.__voltaje_maximo = voltaje_maximo
        else:
            print("El valor no puede ser negativo")
    
    @property
    def amperaje_maximo(self):
        return self.__amperaje_maximo
    
    @amperaje_maximo.setter
    def amperaje_maximo(self,amperaje_maximo):
        if amperaje_maximo > 0:
            self.__amperaje_maximo = amperaje_maximo
        else:
            print("El amperaje no puede ser negativo")