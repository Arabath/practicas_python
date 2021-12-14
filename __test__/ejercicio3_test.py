import unittest
from ejercicio3 import Punto
from excepcion_punto import DistanciaCero
class TestPunto(unittest.TestCase):
    """ Suite-Test de la clase Punto """
    def setUp(self) -> None:
        self.punto1 = Punto(0, 1)
        self.punto2 = Punto(0, 1)

    def test_funcionEsIgual(self):
        """ Verifica que dos puntos sean iguales """

        self.assertTrue(self.punto1.esIgual(self.punto2))

    def test_funcionDistanciaA(self):
        """ Verifica la distancia entre dos puntos """

        self.assertFalse(self.punto1.distanciaA(self.punto2))

if __name__ == "__main__":
    unittest.main()