#calculadora *semi-cientifica*
##Esta *calculadora* es capas de realizar operaciones como 


opciones=1,2,3,4,5,6,7,8,9

while True:
    print("Bienvenido, favor ingresar una de las opciones")
    print("1, para sumar")
    print("2, para restar")
    print("3, para multiplicar")
    print("4, para dividir")
    print(" 5, para potenciar")
    print(" 6, para sacar raiz")
    print(" 7, para sacar el porcentaje")
    print(" 8, para sacar el modulo")
    print(" 9, para promediar")
    opcion=int(input("elegir la opcion"))
    while opcion not in (1,2,3,4,5,6,7,8,9):
        print("favor agregar una opcion valida")
        opcion=input("elegir la opcion")
    if opcion==1:
         while True:
          try:
             nu = float(input("Favor ingresar el primer número que deseas sumar: "))
             num = float(input("Favor ingresar el segundo número: "))
             print(f"el resultado de tu suma fue {nu + num}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==2:
       while True:
          try:
              
             nu = float(input("Favor ingresar el primer número : "))
             num =float(input("Favor ingresar el segundo número: "))

             
             if nu <0 or num <0 :
                 print("favor poner un numero que sea positivo")
                 continue
                
             print(f"el resultado de la resta fue de {nu - num}")
             break
             
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==3:
       
       while True:
          try:
             nu = float(input("Favor ingresar el primer número : "))
             num = float(input("Favor ingresar el segundo número: "))
             print(f"el resultado de tu multiplicacion fue {nu * num}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==4:
        while True:
          try:
             nu = int(input("Favor ingresar el primer número : "))
             num = int(input("Favor ingresar el segundo número: "))
             print(f"el resultado de tu divicion fue {nu / num}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==5:
        while True:
          try:
             nu = float(input("Favor ingresar el número que desea potenciar : "))
             num = float(input("Favor ingresar la potencia : "))
             print(f"el resultado de tu potencia fue {nu ** num}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==6:
        while True:
          try:
             nu = float(input("Favor ingresar el número al que deseas sacarle raiz : "))
             raiz=nu**0.5
             print(f"el resultado de tu raiz fue {raiz}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==7:
    
        
        while True:
          try:
             nu = int(input("Favor ingresar el primer número : "))
             num = int(input("Favor ingresar el porcentaje que desea saber de dicho número: "))
             por=(nu*num)/100
             print(f"el resultado de tu porcentaje fue {por}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")

    if opcion==8:

        while True:
          try:
             nu = int(input("Favor ingresar el primer número : "))
             num = int(input("Favor ingresar el segundo número: "))
             print(f"el resultado de tu modulo fue {nu % num}")
             break
          except ValueError:
            print("Favor ingresar números válidos.")
    if opcion==9:
       while True:
        cantidad = int(input("¿Cuántos valores deseas promediar? "))

        s=0

        for i in range(cantidad):
          numero = float(input(f"Ingrese el valor {i+1}: "))
          s += numero

          promedio = s / cantidad

        print("El promedio es:", promedio)
        break
    
    