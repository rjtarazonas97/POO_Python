class Pikachu:
    tipo = 'Electrico'
    
    
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

pikachu_1 = Pikachu('Jesus', 800, 1000)
pikachu_2 = Pikachu('Juan', 1200, 1002)

print(pikachu_1.tipo,pikachu_1.nombre,pikachu_1.nivel)
print(pikachu_2.tipo,pikachu_2.nombre,pikachu_2.nivel)