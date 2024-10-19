import math

def menu_constantes():
    while True:
        print("\nFunciones de Constantes")
        print("1. math.pi")
        print("2. math.e")
        print("3. math.tau")
        print("4. math.inf")
        print("5. math.nan")
        print("6. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("Constante π:", math.pi)
        elif opcion == '2':
            print("Constante e:", math.e)
        elif opcion == '3':
            print("Constante τ:", math.tau)
        elif opcion == '4':
            print("Valor infinito positivo:", math.inf)
        elif opcion == '5':
            print("Valor no numérico (NaN):", math.nan)
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
