"""
    Ejercicio 3:

        Implemente la clase Punto:
            que represente un punto en el plano de coordenadas (x,y).
        Las instancias de dicha clase deben responder al mensaje:
        👉🏻 distanciaA(otroPunto). Que retorna la distancia entre dos puntos
                usando el teorema de Pitágoras.
        👉🏻 si es igual a otro punto.

        Pista:
            🛠 El metodo abs(un_numero) devuelve el valor absoluto de un numero
            ej:
                abs(2)    >>> 2
                abs(-2)   >>> 2

            🛠 El metodo math.pow(un_numero, 2) eleva un numero al cuadrado
            🛠 El metodo math.sqrt(un_numero) devuelve la raiz cuadrada
            👉🏻 Para hacer uso de estos se debe importar el modulo math incluido en Python

            ej:
                import math

                math.pow(3, 2) >>> 9
                math.sqrt(9)   >>> 3

        Defina los tests de unidad que considere necesarios para esta clase.
        Importante: para los assertEqual() de los test no olvide redondear
        con el metodo round(un_numero, 2) para indicarle cuantos decimales tomar
        en cuenta.

        Algunos test:
            🧪 Dos puntos con las mismas coordenadas
            🧪 Dos puntos con las mismas coordenadas en X
            🧪 Dos puntos con las mismas coordenadas en Y
"""

from excepcion_punto import DistanciaCero

class Punto():
    """ Clase Punto """

    def __init__ (self, cordenada_x: int, cordenada_y: int) -> None:
        self.__cordenadaX = cordenada_x
        self.__cordenadaY = cordenada_y

    @property
    def cordenadaX(self): return self.__cordenadaX

    @property
    def cordenadaY(self): return self.__cordenadaY

    def esIgual(self, otroPunto: Punto) -> bool:
        """
        [+] Retorna True si dos puntos son iguales.
        [+] Retorna False si dos puntos son diferentes.
        """
        return self.cordenadaX == otroPunto.cordenadaX and self.cordenadaY == otroPunto.cordenadaY

    # def distanciaA(self, otroPunto: Punto) -> int:
    #     """
    #     [+] Retorna la distancia a un Punto que recibe como parametro
    #     """
    #     if not self.esIgual(self, otroPunto):
    #         raise DistanciaCero
    #     else:
    #         """"""
            
if __name__ == '__main__':
    # punto1 = Punto(0,1)
    # punto2 = Punto(0,1)