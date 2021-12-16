import unittest
from ejercicio3 import Punto
from ejercicio4 import Circulo

class TestCirculo(unittest.TestCase):
    """ Suite-Test de la clase Circulo """
    def setUp(self) -> None:
        self.punto1 = Punto(4, 2)
        self.circulo1 = Circulo(self.punto1, 2)
        self.punto2 = Punto(4, 3)
        self.circulo2 = Circulo(self.punto2, 2)

    def test_metodoPuntoDentroDeCirculo(self):
        """ Verifica si un punto se encuentra dentro de un circulo determinado """

        self.assertTrue(self.circulo1.puntoDentroDeCirculo(self.punto2), True)


    def test_metodoCirculosIgualesSegunRadio(self):
        """ Verifica si dos circulos son iguales entorno a su radio """

        self.assertTrue(self.circulo1.circulosIgualesSegunRadio(self.circulo2))

    def test_metodoCirculoContieneOtroCirculo(self):
        """ Verifica si un circulo contiene otro circulo dentro """
        punto1 = Punto(4, 2)
        circulo1 = Circulo(punto1, 2)
        punto2 = Punto(4, 2)
        circulo2 = Circulo(punto2, 1)

        self.assertTrue(circulo1.circuloContieneOtroCirculo(circulo2))

    def test_metodoCirculosSuperpuestos(self):
        punto1 = Punto(4, 2)
        circulo1 = Circulo(punto1, 2)
        punto2 = Punto(4, 2)
        circulo2 = Circulo(punto2, 2)

        self.assertTrue(circulo1.circulosSuperpuestos(circulo2))

    def test_metodocirculosSeIntersecan(self):
        punto1 = Punto(4, 2)
        circulo1 = Circulo(punto1, 1)
        punto2 = Punto(4, 2)
        circulo2 = Circulo(punto2, 2)

        self.assertTrue(circulo1.circulosSeIntersecan(circulo2))