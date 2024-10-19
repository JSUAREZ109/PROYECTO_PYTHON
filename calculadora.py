import funciones_basicas
import funciones_math
import JHORMAN_SUAREZ.funciones_trigonometricas as funciones_trigonometricas
import JHORMAN_SUAREZ.funciones_hiperbolicas as funciones_hiperbolicas
import JHORMAN_SUAREZ.funciones_constantes as funciones_constantes
import JHORMAN_SUAREZ.funciones_avanzadas as funciones_avanzadas

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Funciones matemáticas incorporadas")
        print("2. Funciones matemáticas del módulo math")
        print("3. Funciones trigonométricas")
        print("4. Funciones hiperbólicas")
        print("5. Funciones de constantes")
        print("6. Otras funciones avanzadas")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            funciones_basicas.menu_funciones_basicas()
        elif opcion == '2':
            funciones_math.menu_funciones_math()
        elif opcion == '3':
            funciones_trigonometricas.menuTrigonometricas()
        elif opcion == '4':
            funciones_hiperbolicas.menuHiperbolicas()
        elif opcion == '5':
            funciones_constantes.menu_constantes()
        elif opcion == '6':
            funciones_avanzadas.menu_avanzadas()
        elif opcion == '7':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
