


# \033 es ESC inica un comando para dar formato a la salida en consola, aqui se utiliza [H y [J son parametros para el escape, se mueve el cursor a la esquina noroeste de la consola y se limpia la consola desde el cursor hasta fin de pantalla respectivamente.
ASCII_limpiar = "\033[H\033[J"

# Contenido de menus
MenuPrincipal = ["Registro de usuario y carrito de compras","Cálculo de totales y validaciones de stock", "Visualización del resumen de compra", "Informes", "Salir"]
Modulo1 = ["Registro de usuario","Carrito de compras"]

# funcion para mas limpiamente limpiar pantalla sin hacer print cada ves, 'end' en el print evita que se cree una nueva linea luego de limpiar pantalla que es el comportamiento por defecto
def limpiar_consola():
    print(ASCII_limpiar, end="")
    return


# Funcion para normalizar menus y evitar extensivo uso de funciones print()
def menu(titulo, opciones, texto):
    limpiar_consola()
    print(f"          ---------- {titulo} ----------\n\n")
    for i in range(opciones):
        print(f"{i+1}. {texto[i]}\n")
    return

# Simulador de compras en linea
def main():

    while True:
        menu("Menu",5,MenuPrincipal)
        
        opcion = input("seleccione una opcion: ")
        match int(opcion):
            case 1:
                menu("Modulo 1",2,Modulo1)
                input()
            case _:
                return

main()
