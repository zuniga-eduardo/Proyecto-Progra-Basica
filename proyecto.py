# logo de la tienda
logo = r"""
                            /))_
                           /   .\/)
                  _."´´´'_'  \___/  
                 ' /           |
                   \          /
                    | ||~~~| ||
                    ^^^´   ^^^´
"""

mini_logo = r"""
 /))_
/   .\/)
"""

# \033 es ESC inica un comando para dar formato a la salida en consola, aqui se utiliza [H y [J son parametros para el escape, se mueve el cursor a la esquina noroeste de la consola y se limpia la consola desde el cursor hasta fin de pantalla respectivamente.
ASCII_limpiar = "\033[H\033[J"

# Contenido de menus
MenuPrincipal = ["Registro de usuario y carrito de compras","Cálculo de totales y validaciones de stock", "Visualización del resumen de compra", "Informes", "Salir"]
Modulo1 = ["Registro de usuario","Carrito de compras"]

# Diccionario con Usuarios
usuarios = {"cliente1":"clave1","cliente2":"clave2","admin":"123"}



# funcion para mas limpiamente limpiar pantalla sin hacer print cada ves, 'end' en el print evita que se cree una nueva linea luego de limpiar pantalla que es el comportamiento por defecto
def limpiar_consola():
    print(ASCII_limpiar, end="")
    return


# Funcion para normalizar menus y evitar extensivo uso de funciones print() en funcion main()
def menu(titulo, opciones, texto, user=None, error=None):
    limpiar_consola()
    print(f"           ---------- {titulo} ----------")
    if error: 
        print(error+"\n")
    else: print("\n")
    if user: 
        print(user+"\n\n") 
    else: print("\n")
    for i in range(opciones):
        print(f"{i+1}. {texto[i]}\n")
    print("\n\n"+mini_logo)
    print("\033[5A", end="")
    return

# Funcion para imprimir pantalla final
def final(error=None):
    limpiar_consola()
    print("           ---------- Adios ----------\n\n")
    if error:
        print(f"          {error}\n")
    print(logo)
    print("                 Vuelva Pronto!")
    print("------------------------------------------------")
    input()

# Modulo de inicio de sesion
def inicio_sesion(cont):
    user = ["","",False]
    limpiar_consola()
    if cont == 0:
        print(f"           ---------- Bienvenido ----------\n{logo}\n")
    else:
        print(f"           ---------- Inicio de sesion fallido ----------\n{logo}\n")
        print("                       Intente de Nuevo!")
    user[0] = input("                Usuario: ")
    user[1] = input("                  Clave: ")
    if not user[0] in usuarios:
        return user
    if not user[1] == usuarios[user[0]]:
        return user
    user[2] = True
    return user










# Simulador de compras en linea
def main():
    for i in range(3):
        user = inicio_sesion(i)
        if user[2] == True:
            break
        if i == 2: 
            final("Demaciados intentos fallidos")
            return
    
    opcion_invalida = None
    while True:
        menu("Menu",5,MenuPrincipal,user[0],opcion_invalida)
        
        opcion = input("seleccione una opcion: ")    
        try:
            opcion = int(opcion)
        except:
            opcion_invalida = "                 Opcion Invalida"
            continue
        opcion_invalida = None
        match opcion:
            case 1:
                menu("Modulo 1",2,Modulo1,user[0])
                input("seleccione una opcion: ")
            case _:
                final()
                return

main()
