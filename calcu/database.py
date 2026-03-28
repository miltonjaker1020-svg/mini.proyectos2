import json

archivo="historial.json"

def cargar():
    try:
        with open(archivo,"r") as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
    
def guardar(historial):
    with open(archivo,"w") as file:
        json.dump(historial, file)
    
    
def  agregar(operacion):
    historial=cargar()
    historial.append(operacion)
    guardar(historial)
    
def borrar_historial():
    guardar([])
    
    