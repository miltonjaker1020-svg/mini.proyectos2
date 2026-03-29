import os
import json
import random
archivo = 'clientes.json'

def guardar( archivo,usuarios):
    with open(archivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
        
        
def cargar(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []



usuarios=cargar(archivo)

def registrar():
    
    try:
        
        id=random.randint(1000,9999)
        print(f"ID: {id}")
        nuevo_usuario = input("Ingrese el nombre del usuario: ")
            
        while any(u["nombre"] == nuevo_usuario for u in usuarios) or  not nuevo_usuario.isalpha():
            print("El nombre de usuario ya existe. Por favor, ingrese otro nombre.")
            nuevo_usuario = input("Ingrese el nombre del usuario: ")
            
            
            
            
            
            
            
        edad=int(input("Ingrese la edad del usuario: "))
        while edad <0 or edad > 100:
            print("La edad no es válida. Por favor, ingrese una edad válida.")
            edad=int(input("Ingrese la edad del usuario: "))
       
        tipo=input("""ingrese su tipo de plan
                   mensual
                   trimestral
                   anual
                   """).lower()
        
        while tipo not in ["mensual","trimestral","anual"]:
            print("El tipo de plan no es válido. Por favor, ingrese un tipo de plan válido.")
            tipo=input("""ingrese su tipo de plan
                   mensual
                   trimestral   
                   anual
                   """).lower()
            
        estado="activo"
        
        usuario={"id":id,
                 "nombre":nuevo_usuario,
                 "edad":edad,
                 "tipo":tipo,
                 "estado":estado}
        usuarios.append(usuario)
        
        guardar(archivo,usuarios)
        
    except ValueError:
        print("Error al registrar el usuario.")
        
        
        
        
def listar(arhcivo,usuarios):
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Tipo de plan: {usuario['tipo']}")
        print(f"Estado: {usuario['estado']}")
        print("--------------------")
        
        
        
        
def buscar(archivo,usuarios):
    

    cargar(archivo)
    try:
        print("""1. Buscar usuario por ID
                 2. Buscar usuario por nombre""")
        
        respuesta=int(input("Ingrese la opción deseada: "))
        while respuesta not in [1,2]:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            respuesta=int(input("Ingrese la opción deseada: "))
        
        if respuesta==1:
            id=int(input("Ingrese el ID del usuario que desea buscar: "))
            for ids in usuarios:
                if id == ids['id']:
                    print(f"ID: {ids['id']}")
                    print(f"Nombre: {ids['nombre']}")
                    print(f"Edad: {ids['edad']}")
                    print(f"Tipo de plan: {ids['tipo']}")
                    print(f"Estado: {ids['estado']}")
                else:
                    print("No se encontró ningún usuario con ese ID.")
                
        else:
            nombre=input("Ingrese el ID del usuario que desea buscar: ")
            for usuarios in usuarios:
                if nombre == usuarios['nombre']:
                    print(f"ID: {usuarios['id']}")
                    print(f"Nombre: {usuarios['nombre']}")
                    print(f"Edad: {usuarios['edad']}")
                    print(f"Tipo de plan: {usuarios['tipo']}")
                    print(f"Estado: {usuarios['estado']}")
                else:
                    print("No se encontró ningún usuario con ese nombre.")
            
    except ValueError:
        print("Error al buscar el usuario.")
        
        
        
        
def actualizar(archivo,usuarios):
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Tipo de plan: {usuario['tipo']}")
        print(f"Estado: {usuario['estado']}")
        print("--------------------")
        
    try:
        id=int(input("Ingrese el ID del usuario que desea actualizar: "))   
        for ids in usuarios:
            if id == ids['id']:
                print("""que desea actualizar: 
                  1. Nombre
                  2. Edad
                  3. Tipo de plan
                  4. Estado""")
            
            respuesta=int(input("Ingrese la opción deseada: "))
            while respuesta not in [1,2,3,4]:
                print("Opción no válida. Por favor, ingrese una opción válida.")
                respuesta=int(input("Ingrese la opción deseada: "))
                
            if respuesta==1:
                nuevo_nombre=input("Ingrese el nuevo nombre del usuario: ")
                ids['nombre']=nuevo_nombre
                guardar(archivo,usuarios)
                print("El nombre del usuario ha sido actualizado correctamente.")
           
            elif respuesta==2:
                nueva_edad=int(input("Ingrese la nueva edad del usuario: "))
                ids['edad']=nueva_edad
                guardar(archivo,usuarios)
                print("La edad del usuario ha sido actualizada correctamente.")
                
            elif respuesta==3:
                nuevotipo=input("""Ingrese el nuevo tipo de plan del usuario: 
                                 mensual
                                 trimestral
                                 anual
                                 """).lower()
                
                while not nuevotipo.isalpha() or not nuevotipo in ["mensual","trimestral","anual"]:
                    print("El tipo de plan no es válido. Por favor, ingrese un tipo de plan válido.")
                    nuevotipo=input("""Ingrese el nuevo tipo de plan del usuario: 
                                 mensual
                                 trimestral
                                 anual
                                 """).lower()
                ids['tipo']=nuevotipo
                guardar(archivo,usuarios)
                print("El tipo de plan del usuario ha sido actualizado correctamente.")
                
                
            elif respuesta==4:
                nuevoestado=input("""Ingrese el nuevo estado del usuario: 
                                 activo
                                 inactivo
                                 """).lower()
                while not nuevoestado.isalpha() or not nuevoestado in ["activo","inactivo"]:
                    print("El estado no es válido. Por favor, ingrese un estado válido.")
                    nuevoestado=input("""Ingrese el nuevo estado del usuario: 
                                 activo
                                 inactivo
                                 """).lower()
                ids['estado']=nuevoestado
                guardar(archivo,usuarios)
                print("El estado del usuario ha sido actualizado correctamente.")
                
            print("El usuario ha sido actualizado correctamente.")
        else:
            print("No se encontró ningún usuario con ese ID.")
    except ValueError:
        print("Error al actualizar el usuario.")
        
        
        
def eliminar(archivo,usuarios):
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Tipo de plan: {usuario['tipo']}")
        print(f"Estado: {usuario['estado']}")
        print("--------------------")
        
    try:
        id=int(input("Ingrese el ID del usuario que desea eliminar: "))
        for ids in usuarios:
            if id==ids['id']: 
                usuarios.remove(ids)
                guardar(archivo,usuarios)
                print("El usuario ha sido eliminado correctamente.")
            else:
                print("No se encontró ningún usuario con ese ID.")  
                
    except ValueError:
        print("Error al eliminar el usuario.")