"""
    Ejercicio 4:
        La empresa para la que usted trabaja planea desarrollar un software para la visualización de figuras geométricas. Para esto se le pide que:
        a) Modele el concepto de un círculo en términos de su centro y su radio.
        b) Pueda saber si un punto se encuentra dentro de un círculo.
        c) Pueda saber si dos circulos son iguales en torno a su radio.
        d) Pueda saber si un circulo contiene otro circulo.
        e) Pueda saber si dos circulos estan superpuestos.
        f) Pueda saber si dos círculos se intersecan o no.
        g) Generar una excepción en el caso de que el radio pasado como parametro.
            sea menor a 1. ValueError('Radio no valido!.')
        Implemente las clases necesarias y sus tests.
        Puede reutilizar la clase Punto.
"""

from ejercicio3 import Punto
import math
class Circulo():
    """
        Clase Cirulo:
        [+] Recibe 2 parámetros
            - Clase Punto(x,y) con sus coordenadas.
            - radio del circulo.
    """

    def __init__(self, punto: 'Punto', radio: int) -> None:
        self.__punto = punto
        self.__radio = radio

    @property
    def radio(self):
        """ [+] Retorna el radio del circulo seleccionado """
        return self.__radio

    @property
    def perimetro(self):
        """ [+] Retorna el perimetro del circulo seleccionado """
        return self.__radio * math.pi


    # b) Pueda saber si un punto se encuentra dentro de un círculo.
    def puntoDentroDeCirculo(self, punto: 'Punto') -> bool:
        """ [+] Verifica si un punto se encuentra dentro de un circulo """
        distancia = self.__punto.distanciaA(punto)
        if distancia < self.__radio:
            return True
        else:
            return False


    # c) Pueda saber si dos circulos son iguales en torno a su radio.
    def circulosIgualesSegunRadio(self, circulo: 'Circulo') -> bool:
        """ [+] Verifica si dos circulos son igual entorno a su radio """
        return self.__radio == circulo.radio


    # d) Pueda saber si un circulo contiene otro circulo.
    def circuloContieneOtroCirculo(self, circulo: 'Circulo') -> bool:
        """ [+] Verifica si el circulo contiene otro circulo dentro """
        return (self.__punto.distanciaA(circulo.__punto) + circulo.__radio) < self.__radio


    # e) Pueda saber si dos circulos estan superpuestos.
    def circulosSuperpuestos(self, circulo: 'Circulo') -> bool:
        """ [+] Verifica si los circulos se encuentran superpuestos """
        return self.__punto.esIgual(circulo.__punto) and self.circulosIgualesSegunRadio(circulo)


    # f) Pueda saber si dos círculos se intersecan o no.
    def circulosSeIntersecan(self, circulo: 'Circulo') -> bool:
        """ [+] Verifica si los circulos se intersecan """
        return not Circulo(self.__punto, self.__radio).circuloContieneOtroCirculo(circulo) and not Circulo(self.__punto, self.__radio).circulosSuperpuestos(circulo) and self.__punto.distanciaA(circulo.__punto) < (self.__radio + circulo.__radio)


if __name__ == '__main__':
    punto1 = Punto(4, 2)
    circulo1 = Circulo(punto1, 2)

    punto2 = Punto(7, 2)
    circulo2 = Circulo(punto2, 2)

    print(f"[+] CoordenadaX del punto1: {punto1.cordenadaX}")
    print(f"[+] CoordenadaY del punto1: {punto1.cordenadaY}")
    print(f"[+] Radio del circulo del punto1: {circulo1.radio}")
    print(f"[+] Perimetro del circulo del punto1 : {circulo1.perimetro}")
    print("-----")
    print(f"[+] CoordenadaX del punto2: {punto2.cordenadaX}")
    print(f"[+] CoordenadaY del punto2: {punto2.cordenadaY}")
    print(f"[+] Distancia entre puntos: {punto1.distanciaA(punto2)}")
    print("-----")
    print(f"[+] Punto dentro del circulo?: {circulo1.puntoDentroDeCirculo(punto2)}")
    print("-----")
    print(f"[+] Circulos iguales segun radio?: {circulo1.circulosIgualesSegunRadio(circulo2)}")
    print("-----")
    print(f"[+] Circulos contiene otro circulo?: {circulo1.circuloContieneOtroCirculo(circulo2)}")
    print("-----")
    print(f"[+] Circulos se encuetran superpuestos?: {circulo1.circulosSuperpuestos(circulo2)}")
    print("-----")
    print(f"[+] Circulos se intersecan?: {circulo1.circulosSeIntersecan(circulo2)}")