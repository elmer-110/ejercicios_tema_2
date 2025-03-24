from MagiaNumerica import MagiaNumerica
from lanzador import main
def main():
    numeros = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    magia = MagiaNumerica(numeros)
    lista_transformada = magia.magia_numerica()
    print("Lista transformada:", lista_transformada)
    es_valida = magia.verificar_suma(lista_transformada)
    print("La suma es válida:", es_valida)
if __name__ == "__main__":
    main()