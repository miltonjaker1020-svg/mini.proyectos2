from funciones import *

archivo = 'clientes.json'
usuarios=cargar(archivo)

while True:
    print("""1. Registrar usuario
             2. Listar usuarios
             3. Buscar usuario
             4. Actualizar usuario
             5. Eliminar usuario
             6. Salir""")
    
    respuesta=int(input("Ingrese la opción deseada: "))
    while respuesta not in [1,2,3,4,5,6]:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        respuesta=int(input("Ingrese la opción deseada: "))
    
    if respuesta==1:
        registrar()
    elif respuesta==2:
        listar(archivo,usuarios)
    elif respuesta==3:
        buscar(archivo,usuarios)
    elif respuesta==4:
        actualizar(archivo,usuarios)
    elif respuesta==5:
        eliminar(archivo,usuarios)
    elif respuesta==6:
        break