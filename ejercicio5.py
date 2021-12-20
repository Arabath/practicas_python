"""
    Ejercicio 5:
        Para un sistema de cátedras en una facultad se requiere llevar un registro estudiantes y las notas de los parciales que han rendido.
        De cada estudiante se sabe su nombre y apellido.
        Implemente las clases necesarias y sus correspondientes tests para poder contestar a las siguientes preguntas:
        a) Saber si un estudiante aprobó la cursada (la cursada se considera aprobada si todas sus notas son
        mayores o iguales a 4).
        b) Saber si un estudiante promocionó la cursada (la cursada se considera aprobada si todas sus notas
        son mayores o iguales a 7).
        c) Saber la cantidad de notas menores a 4 que sacó un estudiante.
"""

class RegistroAlumnos():
    """
        Clase RegistroAlumnos:
        [+]
    """

    def __init__(self) -> None:
        self.__registro = {"Axel Hobrecht" : [7,7,7], "Ezequiel Salomon" : [5,4,7]}

    @property
    def diccionario(self):
        return self.__registro

    def notas(self, alumno) -> list:
        """ [+] Retorna las notas del alumno pasado como parámetro """
        alumno = self.diccionario[alumno]
        return alumno

    def condicion(self,alumno) -> list:
        """ [+] Retorna True si el alumno aprobó todas las materias """
        notas = self.notas(alumno)
        # if map(lambda x: x >= 4, notas):
        #     return "aprobado"
        # if map(lambda x: x >= 7, notas):
        #     return "promocionado"
        # else:
        #     return "desaprobado"

        if notas >= [4,4,4] and notas < [7,7,7]:
            return "Cursada Aprobada"
        elif notas >= [7,7,7]:
            return "Cursada Promocionada" 
        else:
            return "Cursada Reprobada"    



if __name__ == '__main__':
    registro = RegistroAlumnos()

    # print(registro.diccionario)
    # print(registro.notas("Axel Hobrecht"))
    # print(registro.notas("Ezequiel Salomon"))
    print(registro.condicion("Ezequiel Salomon"))
    print(registro.condicion("Axel Hobrecht"))