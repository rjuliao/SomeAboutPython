from PrimerPrograma.Calculadora import Calculadora

if __name__ == "__main__":
    print("Welcome to Python")
    na = int(input("Ingrese número = "))
    nb = int(input("Ingrese número = "))

    cal = Calculadora(na, nb)
    print("1.-Multiplicar\n2.- Sumar\n3.- Restar\n4.- Dividir")

    op = int(input("Qué desea hacer? :"))

    res = 0

    if op == 1:
        res = cal.multiplicar()
    elif op == 2:
        res = cal.suma(1)
    elif op == 3:
        res = cal.suma(0)
    elif op == 4:
        res = cal.div()


    print("Tu respuesta es: " + str(res))