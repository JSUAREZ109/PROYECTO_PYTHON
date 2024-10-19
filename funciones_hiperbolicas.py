import math

def menuHiperbolicas():
    while True:
        print("\nFunciones Hiperbólicas")
        print("1. math.sinh(x)")
        print("2. math.cosh(x)")
        print("3. math.tanh(x)")
        print("4. math.asinh(x)")
        print("5. math.acosh(x)")
        print("6. math.atanh(x)")
        print("7. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            x = float(input("Introduce un número: "))
            print("Resultado de sinh:", math.sinh(x))
        elif opcion == '2':
            x = float(input("Introduce un número: "))
            print("Resultado de cosh:", math.cosh(x))
        elif opcion == '3':
            x = float(input("Introduce un número: "))
            print("Resultado de tanh:", math.tanh(x))
        elif opcion == '4':
            x = float(input("Introduce un número: "))
            print("Resultado de asinh:", math.asinh(x))
        elif opcion == '5':
            x = float(input("Introduce un número mayor o igual a 1: "))
            if x >= 1:
                print("Resultado de acosh:", math.acosh(x))
            else:
                print("El número debe ser mayor o igual a 1.")
        elif opcion == '6':
            x = float(input("Introduce un número: "))
            print("Resultado de atanh:", math.atanh(x))
        elif opcion == '7':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
