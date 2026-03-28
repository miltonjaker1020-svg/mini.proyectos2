from util import *

while True:
    print("""
1. Registrar coder
2. Ver calificaciones
3. Ver resumen
4. Salir
""")

    opcion = input("Seleccione una opcion: ")
    while opcion not in ("1", "2", "3", "4"):
        print("Opcion no valida")
        opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registro()

    elif opcion == "2":
        calificacion()

    elif opcion == "3":
        resumen()

    elif opcion == "4":
        break