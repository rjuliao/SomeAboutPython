#Las clases y funciones debe ir arriba de la llamada a cada una

#Clase padre
class Human:

    def __init__(self):
        print("human")

    def comer(self):
        print("tengo hambre njda")

#Clase hija
class Woman(Human):

    def __init__(self):
        print("soy una chik")

    def saludar(self):
        print("comer verga")


def algo():
    print("algo puej")