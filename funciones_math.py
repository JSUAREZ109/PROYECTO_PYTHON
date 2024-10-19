import math

def menu_funciones_math():
    while True:
        print("\nFunciones del Módulo math")
        print("1. math.sqrt(x)")
        print("2. math.exp(x)")
        print("3. math.log(x, base)")
        print("4. math.log10(x)")
        print("5. math.log2(x)")
        print("6. math.factorial(x)")
        print("7. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            x = float(input("Introduce un número: "))
            print("Raíz cuadrada:", math.sqrt(x))
        elif opcion == '2':
            x = float(input("Introduce un número: "))
            print("e elevado a x:", math.exp(x))
        elif opcion == '3':
            x = float(input("Introduce un número: "))
            base = input("Introduce la base (dejar en blanco para log natural): ")
            if base == '':
                print("Logaritmo natural:", math.log(x))
            else:
                print("Logaritmo:", math.log(x, float(base)))
        elif opcion == '4':
            x = float(input("Introduce un número: "))
            print("Logaritmo base 10:", math.log10(x))
        elif opcion == '5':
            x = float(input("Introduce un número: "))
            print("Logaritmo base 2:", math.log2(x))
        elif opcion == '6':
            x = int(input("Introduce un número entero: "))
            print("Factorial:", math.factorial(x))
        elif opcion == '7':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
