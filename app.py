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

OPERACIONES = {
    1: ("Suma", suma),
    2: ("Resta", resta),
    3: ("Multiplicación", multiplicacion),
    4: ("División", division),
}

def mostrar_menu():
    print("\n=== Calculadora ejercicio:3.0.0 ===")
    for key, (nombre, _) in OPERACIONES.items():
        print(f"{key}. {nombre}")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese el número de la operación: "))
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
            continue

        if opcion == 5:
            print("✅ Gracias por usar la calculadora. ¡Hasta luego!")
            break

        if opcion not in OPERACIONES:
            print("❌ Opción no válida. Intente de nuevo.")
            continue

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
            continue

        nombre, funcion = OPERACIONES[opcion]
        resultado = funcion(a, b)
        if isinstance(resultado, str):  # caso de error en división
            print(resultado)
        else:
            print(f" Resultado de la {nombre}: {resultado:.2f}")

if __name__ == "__main__":
    main()
