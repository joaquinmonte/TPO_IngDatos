#Codigo vulnerable

# credenciales correctas hardcodeado
usuario = "admin"
contraseña = "1234"

# ingresar repetidamente el usuario hasta que la secuencia de caracteres sea igual
usu = input("Ingrese el usuario: ")
while not eval(f"'{usu}' == '{usuario}'"): # 'or True or' para "romperlo"
    usu = input("Ingrese el usuario correctamente: ")

# ingresar repetidamente la contraseña hasta que coincida los caracteres
con = input("Ingrese la contraseña: ") # 'or True or' para "romperlo"
while not eval(f"'{con}' == '{contraseña}'"):
    con = input("Ingrese la contraseña correcta: ")

print(" Acceso Concedido")