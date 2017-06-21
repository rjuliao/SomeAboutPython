
class Calculadora:

    numa = 0
    numb = 0

    #Método constructor
    def __init__(self, numa, numb):
        self.numa = numa
        self.numb = numb

    def multiplicar(self):

        mult = self.numa * self.numb

        return mult

    def suma(self, signo):

        if signo == 1:
            return  self.numa + self.numb
        else:
            return  self.numa - self.numb


    def div(self):

        if self.numb == 0:
            print("No se puede dividir entre 0.")
        else:
            return self.numa/self.numb


    #Metodos para obtener el calor de una atributo
    def getNuma(self):
        return self.numa

    def getNumb(self):
        return self.numb

    #Metodos para cambiar el valor de un atributo
    def setNumb(self, numb):
        self.numb = numb

    def setNuma(self, numa):
        self.numa = numa
