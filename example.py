import human


def paula():
    print("Esto hace algo")

def ema():
    print("Esto hace algo x2")

#Función main
#Si una función se encuentra debajo del main, no será encontrada.
if __name__=="__main__":
    print("hello again")
    paula()
    ema()
    h = human.Human() #La forma correcta de llamar una clase que esta en otro módulo
    h.comer()
    human.algo() #Forma de llamar una función que esta dentro de un módulo
    g = human.Woman()


#class human:

#   def __init__(self):
#      print("Soy humano")