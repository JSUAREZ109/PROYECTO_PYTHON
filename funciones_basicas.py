def menu_funciones_basicas():
    while True:
        print("\nFunciones Matemáticas Incorporadas")
        print("1. abs(x)")
        print("2. round(x, n)")
        print("3. pow(x, y)")
        print("4. divmod(x, y)")
        print("5. sum(iterable)")
        print("6. min(iterable)")
        print("7. max(iterable)")
        print("8. Regresar al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            x = float(input("Introduce un número: "))
            print("Valor absoluto:", abs(x))
        elif opcion == '2':
            x = float(input("Introduce un número: "))
            n = int(input("Introduce el número de decimales: "))
            print("Número redondeado:", round(x, n))
        elif opcion == '3':
            x = float(input("Introduce x: "))
            y = float(input("Introduce y: "))
            print("Resultado de x elevado a y:", pow(x, y))
        elif opcion == '4':
            x = float(input("Introduce x: "))
            y = float(input("Introduce y: "))
            cociente, resto = divmod(x, y)
            print(f"Cociente: {cociente}, Resto: {resto}")
        elif opcion == '5':
            iterable = input("Introduce números separados por comas: ")
            numeros = [float(i) for i in iterable.split(",")]
            print("Suma:", sum(numeros))
        elif opcion == '6':
            iterable = input("Introduce números separados por comas: ")
            numeros = [float(i) for i in iterable.split(",")]
            print("Mínimo:", min(numeros))
        elif opcion == '7':
            iterable = input("Introduce números separados por comas: ")
            numeros = [float(i) for i in iterable.split(",")]
            print("Máximo:", max(numeros))
        elif opcion == '8':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
