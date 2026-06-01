import sys

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return "Error: división por cero" if b == 0 else a / b

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

def modo_interactivo():
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

        if opcion not in OPERACIONES:
            print(" Opción no válida. Intente de nuevo.")
            continue

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print(" Entrada inválida. Debe ser un número.")
            continue

        nombre, funcion = OPERACIONES[opcion]
        resultado = funcion(a, b)
        print(f" Resultado de la {nombre}: {resultado:.2f}" if not isinstance(resultado, str) else resultado)

def modo_automatico():
    if len(sys.argv) < 4:
        print("Uso: python app.py <operacion> <a> <b>")
        print("Operaciones disponibles: suma, resta, multiplicacion, division")
        return

    operacion = sys.argv[1].lower()
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    except ValueError:
        print(" Los números deben ser válidos.")
        return

    funciones = {
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicacion,
        "division": division,
    }

    if operacion not in funciones:
        print(" Operación no válida.")
        return

    resultado = funciones[operacion](a, b)
    print(f" Resultado de la {operacion}: {resultado}" if not isinstance(resultado, str) else resultado)

if __name__ == "__main__":
    # Si se pasan argumentos, usa modo automático
    if len(sys.argv) > 1:
        modo_automatico()
    else:
        modo_interactivo()
