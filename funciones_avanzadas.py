import math

def menu_avanzadas():
    while True:
        print("\nOtras Funciones Avanzadas")
        print("1. math.degrees(x)")
        print("2. math.radians(x)")
        print("3. math.dist(p, q)")
        print("4. math.erf(x)")
        print("5. math.erfc(x)")
        print("6. math.gamma(x)")
        print("7. math.lgamma(x)")
        print("8. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            x = float(input("Introduce un ángulo en radianes: "))
            print("Grados:", math.degrees(x))
        elif opcion == '2':
            x = float(input("Introduce un ángulo en grados: "))
            print("Radianes:", math.radians(x))
        elif opcion == '3':
            p = list(map(float, input("Introduce las coordenadas de p (x, y): ").split(",")))
            q = list(map(float, input("Introduce las coordenadas de q (x, y): ").split(",")))
            print("Distancia euclidiana:", math.dist(p, q))
        elif opcion == '4':
            x = float(input("Introduce un número: "))
            print("Función de error gaussiana:", math.erf(x))
        elif opcion == '5':
            x = float(input("Introduce un número: "))
            print("Función complementaria de error:", math.erfc(x))
        elif opcion == '6':
            x = float(input("Introduce un número: "))
            print("Función gamma:", math.gamma(x))
        elif opcion == '7':
            x = float(input("Introduce un número: "))
            print("Logaritmo natural de la función gamma:", math.lgamma(x))
        elif opcion == '8':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
