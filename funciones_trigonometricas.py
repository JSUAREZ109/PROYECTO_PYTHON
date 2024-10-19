import math

def menuTrigonometricas():
    while True:
        print("\nFunciones Trigonométricas")
        print("1. math.sin(x)")
        print("2. math.cos(x)")
        print("3. math.tan(x)")
        print("4. math.asin(x)")
        print("5. math.acos(x)")
        print("6. math.atan(x)")
        print("7. math.atan2(y, x)")
        print("8. math.hypot(x, y)")
        print("9. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de sin:", math.sin(x))
        elif opcion == '2':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de cos:", math.cos(x))
        elif opcion == '3':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de tan:", math.tan(x))
        elif opcion == '4':
            x = float(input("Introduce un número (entre -1 y 1): "))
            if -1 <= x <= 1:
                print("Resultado de asin:", math.asin(x))
            else:
                print("El número debe estar entre -1 y 1.")
        elif opcion == '5':
            x = float(input("Introduce un número (entre -1 y 1): "))
            if -1 <= x <= 1:
                print("Resultado de acos:", math.acos(x))
            else:
                print("El número debe estar entre -1 y 1.")
        elif opcion == '6':
            x = float(input("Introduce un número: "))
            print("Resultado de atan:", math.atan(x))
        elif opcion == '7':
            y = float(input("Introduce el valor de y: "))
            x = float(input("Introduce el valor de x: "))
            print("Resultado de atan2:", math.atan2(y, x))
        elif opcion == '8':
            x = float(input("Introduce el valor de x: "))
            y = float(input("Introduce el valor de y: "))
            print("Resultado de hypot:", math.hypot(x, y))
        elif opcion == '9':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
