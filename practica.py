my_variable = "mi variable"
my_variable= "nueva variablee"
my_constant = "mi constante"

My_int = 1
My_float = 1.2
My_bool = True
My_bool = False
My_string = "mi cadena de texto"
My_otherstring = "mi otra cadena de texto"

def dividir(a,b):
    if b == 0:
        return "no se puede divider entre 0"
    
def calculadora():
  while True:
    print("bienvenido porfavor escoga una opcion")
    print("1 para sumar")
    print("2 para restar")
    print("3 para dividir")
    print("4 para multiplicar")
   
  
    opcion= int(input("favor ingresar una de las opciones"))
    if opcion not in(1,2,3,4):
            print("favor ingresar una de las opciones")
            continue
    
            
         
    a= int(input("ingrese el primer numero"))
    b= int(input("ingrese su segundo numero"))
    if opcion == 1:
            print("el resultado es", a + b)
            
    elif opcion== 2:
            print(f"el resultado es, {a - b} ")
            
     
    elif opcion== 3:
            print(f"el resultado es", dividir(a,b))
        
    elif opcion== 4:
            print(f"el resultado es, {a * b}")
            
    else:
            print("pon una opcion valida")
            continue

    
calculadora()
        
 

