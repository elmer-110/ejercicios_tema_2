class MagiaNumerica:
    def __init__(self, numeros):
        self.numeros = numeros

    def eliminar_duplicados(self):
        return list(set(self.numeros))

    def ordenar_mayor_a_menor(self, lista):
        return sorted(lista, reverse=True)

    def eliminar_impares(self, lista):
        return [num for num in lista if num % 2 == 0]

    def sumar_numeros(self, lista):
        return sum(lista)

    def magia_numerica(self):
        lista_sin_duplicados = self.eliminar_duplicados()
        lista_ordenada = self.ordenar_mayor_a_menor(lista_sin_duplicados)
        lista_sin_impares = self.eliminar_impares(lista_ordenada)
        suma = self.sumar_numeros(lista_sin_impares)
        lista_final = [suma] + lista_sin_impares
        return lista_final

    def verificar_suma(self, lista):
        return lista[0] == sum(lista[1:])