#Codigo seguro

# credenciales correctas hardcodeado
usuario = "admin"
contraseña = "1234"

contador = 1
ingreso_invalido = False

usu = input("Ingrese el usuario: ")
while usu != usuario and contador < 4:
    usu = input("Ingrese el usuario correctamente: ")
    contador= contador + 1
    if contador == 4:
        ingreso_invalido = True

if ingreso_invalido == False:
    contador = 1
    con = input("Ingrese la contraseña: ")
    while con != contraseña and contador < 4:
        con = input("Ingrese la contraseña correcto: ")
        contador= contador + 1
        if contador == 4:
            ingreso_invalido = True
            break
        
    if ingreso_invalido== False:      
        print(" Acceso Concedido")
    else:
        print ("Se ah sobrepasado el maximo de intentos")

else:
    print ("Se ah sobrepasado el maximo de intentos")