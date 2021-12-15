"""
    Ejercicio 4:
        La empresa para la que usted trabaja planea desarrollar un software para la visualización
         de figuras geométricas. Para esto se le pide que:
        a) Modele el concepto de un círculo en términos de su centro y su radio.
        b) Pueda saber si un punto se encuentra dentro de un círculo.
        c) Pueda saber si dos circulos son iguales en torno a su radio.
        d) Pueda saber si un circulo contiene otro circulo.
        e) Pueda saber si dos circulos estan superpuestos.
        f) Pueda saber si dos círculos se intersecan o no.
        g) Generar una excepción en el caso de que el radio pasado como parametro 
            sea menor a 1. ValueError('Radio no valido!.')

        Implemente las clases necesarias y sus tests.
        Puede reutilizar la clase Punto.
"""
from ejercicio3 import Punto
class Circulo():
    """ Clase circulo """

    def __init__(self, punto: 'Punto', radio: int) -> None:
        self.__punto = punto
        self.__radio = radio

    @property
    def cordenadaX(self): return self.__punto.cordenadaX
    @property
    def cordenadaY(self): return self.__punto.cordenadaY

    @property
    def radio(self): return self.__radio


if __name__ == "__main__":
    punto1 = Punto(3,2)
    circulo1 = Circulo(punto1, 6)
    punto2 = Punto(2,2)
    circulo2 = Circulo(punto2, 2)

    
print(circulo1.cordenadaX)
print(circulo1.cordenadaY)
print(circulo1.radio)

print(circulo2.cordenadaX)
print(circulo2.cordenadaY)
print(circulo2.radio)


