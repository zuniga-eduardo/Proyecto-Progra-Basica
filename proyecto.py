# ------------------------------------
#   LOGOS
# ------------------------------------
# logo principal
logo = r"""
                            /))_
                           /   .\/)
                  _."´´´'_'  \___/  
                 ' /           |
                   \          /
                    | ||~~~| ||
                    ^^^´   ^^^´
"""

# mini logo
mini_logo = r"""
 /))_
/   .\/)
"""





# ------------------------------------
#   VARIABLES GLOBALES
# ------------------------------------

# \033 es ESC inica un comando para dar formato a la salida en consola, aqui se utiliza [H y [J son parametros para el escape, se mueve el cursor a la esquina noroeste de la consola y se limpia la consola desde el cursor hasta fin de pantalla respectivamente.
ASCII_limpiar = "\033[H\033[J"

### Contenido de menus
MenuPrincipal = ["Registro de usuario y carrito de compras","Cálculo de totales y validaciones de stock", "Visualización del resumen de compra", "Informes", "Salir"]

Modulo1 = ["Registro de usuario","Carrito de compras","Salir"]
Modulo2 = ["Calculo de carrito","Validacion de stock","Salir"]


# Diccionario con Usuarios
usuarios = {
    "cliente1":"clave1",
    "cliente2":"clave2",
    "admin":"123",
    "1":"1"
    }

# lista con stock base de la tienda
# cada sublista tiene la estructura:
# 1- Nombre producto 2- Precio en dolares del producto 3- cantidad en stock del producto
stock_base = [
    ["Arroz", 2.50, 1],
    ["Frijoles", 1.80, 42],
    ["Leche", 1.20, 25],
    ["Pan", 1.50, 30],
    ["Huevos", 2.10, 50],
    ["Queso", 3.75, 18],
    ["Pollo", 5.40, 22],
    ["Carne", 6.80, 15],
    ["Manzanas", 2.30, 28],
    ["Bananos", 1.10, 35],
    ["Naranjas", 2.00, 27],
    ["Tomates", 1.90, 33],
    ["Cebollas", 1.60, 0],
    ["Papas", 2.20, 40],
    ["Aceite", 4.50, 12],
    ["Azucar", 1.70, 26],
    ["Sal", 0.90, 45],
    ["Cafe", 5.00, 17],
    ["Galletas", 2.60, 29]
]







# ------------------------------------
#   FUNCIONES
# ------------------------------------

# funcion para mas limpiamente limpiar pantalla sin hacer print cada ves, 'end' en el print evita que se cree una nueva linea luego de limpiar pantalla que es el comportamiento por defecto
def limpiar_consola():
    print(ASCII_limpiar, end="")
    return

# Funcion para imprimir el mini logo en la parte izquierda de consola, luego se regresa 5 filas arriba
"""
Ex. 
mini_logo_menu()
input("Linea nueva aqui")

output:
Linea nueva aqui: 

 /))_
/   .\/)
"""
def mini_logo_menu():
    print("\n\n"+mini_logo)
    print("\033[5A", end="")


# Funcion para normalizar menus y evitar extensivo uso de funciones print() en funcion main()
# Parametros
# - string user | Puede presentar un nombre de usuario en la esquina izquierda
# - string error| Escribe un mensaje de error a pantalla en la parte superior del menu, Ex. cuando se escoge una opcion invalida en menu error = "                 Opcion Invalida"
def menu(titulo, opciones, user=None, error=None):
    limpiar_consola()
    print(f"           ---------- {titulo} ----------")
    if error: 
        print(error+"\a\n")
    else: print("\n")
    if user: 
        print(user+"\n\n") 
    else: print("\n")
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}\n")
    mini_logo_menu()
    error = None
    return error


# Funcion para imprimir pantalla final con logo principal
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
    # [0] = nombre de usuario, [1] = clave de usuario, [2] = false si inicio de sesion fallido y visceversa
    user = ["","",False]
    limpiar_consola()
    if cont == 0:
        print(f"           ---------- Bienvenido ----------\n{logo}\n")
    else:
        print(f"           ---------- Inicio de sesion fallido ----------\n{logo}\n")
        print("                       Intente de Nuevo!")
    user[0] = input("                Usuario: ")
    user[1] = input("                  Clave: ")
    
    # si usuario no existe regresa objeto con false
    if not user[0] in usuarios:
        return user
    
    # si clave incorrecta regresa objeto con false
    if not user[1] == usuarios[user[0]]:
        return user
    
    # Regresa True para inicio de sesion exitoso
    user[2] = True
    return user


# Valida que la opcion seleccionada en un menu sea de tipo int, regresa el valor si si era int o regresa False en caso que no
# Parametros
# - string mensaje  | si la opcion no se a pedido antes poner un mensaje aqui invoca input(mensaje)
# - Any | opcional, si no se declara se pide input(mensaje)  
def validar_opcion(mensaje= "seleccione una opcion: ", opcion=None):
    if not opcion:
        opcion = input(mensaje)    
    try:
        opcion = int(opcion)
        return opcion
    except:
        return False




# ++++++++ Funciones modulo 2 ++++++++


# Funcion que regresa la suma del precio de todos los items en una lista anidada de tipo [["Nombre producto",2.5,1]] donde [1] = precio y [2] = cantidad del producto (tanto stock_base como carrito son ejemplos donde se usa)
def calculo_items(carrito):
    total = 0
    for i in range(len(carrito)):
        # si item esta agotado y marcado para eliminar con "--" en precio o cantiad de 0 no se suma el item
        if carrito[i][1] != "--" and carrito[i][2] != 0: 
            total += (carrito[i][1] * carrito[i][1])
    return round(total,2)

# METODO 1 MODULO 2
# Funcion para mostrar a consola los items en carrito y el precio de estos  
def carrito_actual(carrito):
    limpiar_consola()
    print("           ---------- Valor de Carrito actual ----------\n")
    print(f"           Items en carrito:         {len(carrito)}")
    print(f"           Precio del carrito:      ${calculo_items(carrito)}\n")
    mini_logo_menu()
    input("       Presione enter para volver ")

# METODO 2 MODULO 2
# Funcion para validar stock, imprimir a pantalla y permitir a usuario agregar productos a carrito
def validacion_stock(stock):
    """
    Solo 8 items por pagina, si usuario selecciona 's' se muestran los siguientes 8, si se llega al final de la lista se reinicia a 0 y se imprimen los primeros 8 de nuevo
    Si se selecciona 'r' se regresa a menu
    Si opcion es diferente se valiad que sea int y se imprime mensaje de opcion invalida a pantalla 
    Si opcion es int se valida que el producto no tenga valor de precio de "--" ni cantidad de 0, si lo hace producto agotado y se deja saber al usuario, si no esta agotado se agrega a carrito
    """
    cont = 0
    comentario = None
    # Esta lista contiene los items agregados para comprar que se agregaran al carrito
    lista = []

    while True:
        limpiar_consola()
        print(f"           ---------- Stock ----------\n")
        if comentario:
            print(f"\033[1A{comentario}\n")
            comentario = None
        for i in range(cont,len(stock)):
            if stock[i][2] == 0 and stock[i][1] != "--":
                stock[i][1] = "--"
            if i % 2 == 0:
                print(f"\033[6G{i}. {stock[i][0]}\033[20G{stock[i][1]}$", end="")
            else:    
                print(f"\033[30G{i}. {stock[i][0]}\033[43G{stock[i][1]}$\n")
            cont = i            
            if i != 0 and (i+1) % 8 == 0:
                break
        if i == (len(stock)-1):
            print("\n")
        print("\n   [s] Siguiente pagina | [r] Regresar al menu\n")
        mini_logo_menu()
        opcion = input("Seleccione una opcion para agregarla al carrito: ")

        # cambiar a siguiente pagina
        if opcion.lower() == 's':
            if cont >= (len(stock)-1):
                cont = 0
            else:
                cont += 1
            continue

        # regresar a menu anterior
        if opcion.lower() == 'r':
            return lista

        # Validar opcion es int
        opcion = validar_opcion(opcion=opcion)
        if  opcion is False:
            comentario = "                 Opcion invalida"
            cont = 0
            continue

        # Valor no aceptado imprimir mensaje
        if stock[opcion][2] == 0:
            comentario = "                Producto agotado"
            cont = 0
            continue

        # Agregar item seleccionado a lista y remover 1 unidad del stock, indicar agregado con exito y reiniciar pagina a 0
        lista.append(stock[opcion])
        stock[opcion][2] -= 1
        comentario = "           Producto agregado al carrito"
        cont = 0

# Funcion para comparar listas y agregar solo los productos no repetidos, si producto ya esta en la lista_original se agrega 1 al contador de cantidad del producto 
def agregar_lista(lista_original,lista):
    for i in range(len(lista)):
        if lista[i][0] in str(lista_original):
            index = next(((i, sub.index(lista[i][0])) for i, sub in enumerate(lista_original) if lista[i][0] in sub), None)
            lista_original[index][2] +=1
        else:
            lista_original.append(lista[i])
            lista_original[len(lista_original)-1][2] = 1


            


# ------------------------------------
#   ENTRADA AL PROGRAMA
# ------------------------------------

# Simulador de compras en linea
def main():
    # Variable usada para determinar si mostrar mensaje de opcion erronea en menus
    opcion_invalida = None
    carrito = []
    stock = stock_base

    # Modulo de inicio de sesion
    for i in range(3):
        user = inicio_sesion(i)
        if user[2] == True:
            break
        if i == 2: 
            final("Demaciados intentos fallidos")
            return
    
    # Ciclo de menu principal
    while True:
        opcion_invalida = menu("Menu",MenuPrincipal,user[0],opcion_invalida)

        opcion = validar_opcion()
        if not opcion:
            opcion_invalida = "                 Opcion Invalida"
            continue
        
        match opcion:
            case 1:
                return
            case 2:
                while True:
                    opcion_invalida = menu("Modulo 2",Modulo2,user[0],opcion_invalida)

                    opcion = validar_opcion()
                    if not opcion:
                        opcion_invalida = "                 Opcion Invalida"
                        continue 

                    if opcion == 1:
                        carrito_actual(carrito)
                    elif opcion == 3:
                        break
                    else:
                        nuevo_carrito = validacion_stock(stock)
                        if nuevo_carrito == []:
                            continue
                        agregar_lista(carrito,nuevo_carrito)
            case 3:
                return
            case 4:
                return   
            case 5:
                final()
                return



main()
