class DistanciaCero(Exception):
    """  """
    pass

if __name__ == '__main__':
    try:
        raise DistanciaCero({"mensaje": "Error de distancia"})
    except DistanciaCero as error:
        mensaje = error.args[0]
        print(mensaje["mensaje"])    