import math
from Estrella import Estrella 
from galaxia import Galaxia
def distancia(estrellla1,estrella2):
    def galaxia(estrella):
        def distancia(estrellas):
            def calcular_distancia(e1, e2):
                return math.sqrt((e1.x - e2.x)**2 + (e1.y - e2.y)**2 + (e1.z - e2.z)**2)

            # Crear estrellas
            A = Estrella(2, 3, 1)
            B = Estrella(4, 4, 4)
            C = Estrella(-3, -1, 0)

            # Imprimir estrellas
            print(f"Estrella A: {A}")
            print(f"Estrella B: {B}")
            print(f"Estrella C: {C}")

            # Determinar galaxias
            galaxia_A = Galaxia.determinar_galaxia(A)
            galaxia_B = Galaxia.determinar_galaxia(B)
            galaxia_C = Galaxia.determinar_galaxia(C)

            print(f"Estrella A está en la galaxia: {galaxia_A}")
            print(f"Estrella B está en la galaxia: {galaxia_B}")
            print(f"Estrella C está en la galaxia: {galaxia_C}")

            # Calcular y mostrar distancias
            distancia_AB = calcular_distancia(A, B)
            distancia_BC = calcular_distancia(B, C)

            print(f"Distancia entre A y B: {distancia_AB}")
            print(f"Distancia entre B y C: {distancia_BC}")

            # Encontrar la estrella más lejos del origen
            distancia_origen_A = calcular_distancia(A, Estrella(0, 0, 0))
            distancia_origen_B = calcular_distancia(B, Estrella(0, 0, 0))
            distancia_origen_C = calcular_distancia(C, Estrella(0, 0, 0))

            max_distancia = max(distancia_origen_A, distancia_origen_B, distancia_origen_C)
            if max_distancia == distancia_origen_A:
                estrella_lejos = "A"
            elif max_distancia == distancia_origen_B:
                estrella_lejos = "B"
            else:
                estrella_lejos = "C"

            print(f"La estrella más lejos del origen es: {estrella_lejos}")