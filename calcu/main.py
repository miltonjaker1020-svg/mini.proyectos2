from database import agregar, cargar, borrar_historial

def menu():
    while True:
        print("""
        ===== CALCULADORA PRO =====
        1. Sumar
        2. Restar
        3. Ver historial
        4. Borrar historial
        5. Salir
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            operar("+")
        elif opcion == "2":
            operar("-")
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            borrar_historial()
            print("Historial borrado.")
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opción inválida")

def operar(tipo):
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))

    if tipo == "+":
        resultado = num1 + num2
    elif tipo == "-":
        resultado = num1 - num2

    print("Resultado:", resultado)

    operacion = {
        "num1": num1,
        "num2": num2,
        "operacion": tipo,
        "resultado": resultado
    }

    agregar(operacion)

def ver_historial():
    historial = cargar()

    if not historial:
        print("No hay operaciones registradas.")
        return

    for i, op in enumerate(historial, 1):
        print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']}")

menu()