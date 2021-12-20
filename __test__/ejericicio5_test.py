import unittest
from ejercicio5 import RegistroAlumnos

class TestRegistroAlumnos(unittest.TestCase):
    """ suite-test de la clase RegistroAlumnos """
    def setUp(self) -> None:
        self.registro = RegistroAlumnos()
        self.diccionario = self.registro.diccionario
       

    def test_metodoDiccionario(self):
        """ Verifica si el diccionario de alumnos es correcto """
        
        self.assertEqual(self.diccionario, {"Axel Hobrecht": [7,7,7], "Ezequiel Salomon":[5,4,7]})

    def test_metodoNotas(self):
        """ Verifica que se retornen las notas correspondientes """

        self.assertEqual(self.registro.notas("Axel Hobrecht"), [7,7,7])
        self.assertEqual(self.registro.notas("Ezequiel Salomon"), [5,4,7])
