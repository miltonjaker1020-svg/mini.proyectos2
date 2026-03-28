import json
import os

def cargar():
    if os.path.exists("coders.json"):
        with open("coders.json", "r") as f:
            return json.load(f)
    return {}

def guardar(coders):
    with open("coders.json", "w") as f:
        json.dump(coders,f,indent=4)

coders=cargar()









def registro():
    
        print("""sistema de calificaciones Riwi""")
        
        coder=input("porfavor podrias darnos tu nombre???,:  ").strip()
        while not coder.isalpha():
            print("solo ingrese letras porfavor")
            coder=input("porfavor podrias darnos tu nombre???,:  ").strip()
        if coder not in coders:
            coders[coder] = {"desarrollo": 0, "habilidades": 0, "ingles": 0,
                             "resultado_final": 0} 



        print("""Modulos que se evaluan con sus respectivos numeros de accion
        1.desarrolo
        2. habilidades
        3. Ingles
        """)
      

        opcion=input("favor escoger una de las opciones")
     
        while opcion not in (1,2,3):
            print("favor escoger una de las opciones validas")
            opcion=input("favor escojer una de las opciones")
            while not opcion.isdigit():
                print("solo se permiten numeros enteros")
                opcion=input("favor escojer una de las opciones")
            opcion=int(opcion)
            
        nota = int(input("Ingrese la nota (0-100): "))
        while nota not in range(0, 101):
            print("Solo puedes ingresar notas entre 0 y 100")
            nota = int(input("Ingrese la nota (0-100): "))

        if opcion==1:
            coders[coder]["desarrollo"]=nota
        
        elif opcion==2:
            coders[coder]["habilidades"]=nota
        elif opcion==3:
            coders[coder]["ingles"]=nota
        resultado_final = (coders[coder]["desarrollo"]*0.60 + coders[coder]["habilidades"]*0.20 + coders[coder]["ingles"] * 0.20)
        coders[coder]["resultado_final"] = resultado_final
        if resultado_final >= 80:
            print("Estado: APROBADO")
        elif resultado_final >=50 and resultado_final < 79:
            print("Estado: REGULAR")
        else:
            print("Estado: REPROBADO")
        
        
        guardar(coders)
        print(f"registro actualizadoS")
        
        
def calificacion():
    print("""Bienvenido desea:
          1. Saber su calificacion actual
          2. Saber calificaion de todos los coders""")
    
    opcion=int(input("favor ingresar una de las opciones"))
    while opcion not in range(1,3):
        print("escoga una opcion valida")
        opcion=int(input("favor ingresar una de las opciones"))
    
    if opcion==1:
       coder=input("porfavor podrias darnos tu nombre???,:  ").strip()
       if coder in coders:
            print(f"tu calificacion es {coders[coder]['resultado_final']}")
    
    
    
    
    elif opcion==2:
        for coder, notas in coders.items():
            print(f"{coder}: {notas}")
            
            
            

def resumen():
    print("\nResumen general del módulo")

    total = 0
    cantidad = len(coders)

    for coder, notas in coders.items():
        total += notas["resultado_final"]

    if cantidad > 0:
        promedio = total / cantidad
        print(f"Promedio general: {promedio:.2f}")

    for coder, notas in coders.items():
        print(f"{coder}: {notas['resultado_final']}")