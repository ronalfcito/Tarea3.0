def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def mostrar_menu():
    print("\n=== Calculadora ejercicio:3.0.0 ===")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese el número de la operación: "))
        except ValueError:
            print(" Entrada inválida. Debe ser un número.")
            continue

        if opcion == 5:
            print(" Gracias por usar la calculadora. ¡Hasta luego!")
            break

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print(" Entrada inválida. Debe ser un número.")
            continue

        if opcion == 1:
            print(" Resultado:", suma(a, b))
        elif opcion == 2:
            print(" Resultado:", resta(a, b))
        elif opcion == 3:
            print(" Resultado:", multiplicacion(a, b))
        elif opcion == 4:
            print(" Resultado:", division(a, b))
        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
