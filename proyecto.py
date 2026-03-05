


# \033 es ESC inica un comando para dar formato a la salida en consola, aqui se utiliza [H y [J son parametros para el escape, se mueve el cursor a la esquina noroeste de la consola y se limpia la consola desde el cursor hasta fin de pantalla respectivamente.
ASCII_limpiar = "\033[H\033[J"



# funcion para mas limpiamente limpiar pantalla sin hacer print cada ves, 'end' en el print evita que se cree una nueva linea luego de limpiar pantalla que es el comportamiento por defecto
def limpiar_consola():
    print(ASCII_limpiar, end="")
    return



def main():

    while True:
        print("---------- Menu ----------\n\n")
        print("opcion 1\n")
        print("opcion 2\n")
        print("opcion 3\n")
        opcion = input("seleccione una opcion: ")
        match int(opcion):
            case 1:
                limpiar_consola()
                print("---------- SubMenu ----------\n\n")
                print("Nuevo menu")
                input()
                limpiar_consola()
            case _:
                return

main()