import math
from Estrella import Estrella
from galaxia import Galaxia
from lanzador import Lanzador
class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia A"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia B"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia C"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia D"
        else:
            return "Galaxia desconocida"

    def distancia(self, otra_estrella):
        return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)

# Ejemplo de uso
estrella1 = Estrella(1, 2, 3)
estrella2 = Estrella(4, 5, 6)

print(estrella1)  # Output: (1, 2, 3)
print(estrella1.galaxia())  # Output: Galaxia A
print(estrella1.distancia(estrella2))  # Output: 5.196152422706632