import random
detalleCompra=[[],[],[],[],[],[],[],[]]

def menuOpciones():
    print("¿Que acción desea realizar: ?")
    print("1) Registrar pedido")
    print("2) Mostrar pedidos")
    print("3) Búscar pedido")
    print("4) Salir")
    return int(input("Ingrese la opción: "))


def ingresarPedidos():
    print("--- Nuevo pedido ----")
    print("--- Datos del cliente -----")
    nombreC= input("Nombre: ")
    apellidoC= input("Apellido: ")
    telefonoC= input("Teléfono: ")
    print("--- Datos de la policrush -----")
    nombreP= input("Nombre: ")
    dependenciaP= input("Dependencia: ")
    celularP= input("Celular: ")
    detalleCompra[0].append(nombreC)
    detalleCompra[1].append(apellidoC)
    detalleCompra[2].append(telefonoC)
    detalleCompra[3].append(nombreP)
    detalleCompra[4].append(dependenciaP)
    detalleCompra[5].append(celularP)
    detalleCompra[6].append(random.randrange(1000,9999))
    print("Seleccione el regalo")
    print("1) Opción 1: Poliflor + Polipeluche = $2.50")
    print("2) Opción 2: Poliflor + Policarta = $1.50")
    print("3) Opción 3: Poliflor + Polillavero = $2.00")
    print("4) Opción 4: Poliflor + Polivaso = $2.75")
    opcion = int(input("Ingrese la opción: "))
    if opcion==1:
        detalleCompra[7].append(2.50+(0.1*2.50))
    elif opcion==2:
        detalleCompra[7].append(1.50+(0.1*1.50))
    elif opcion==3:
        detalleCompra[7].append(2.00+(0.1*2.00))
    elif opcion==4:
        detalleCompra[7].append(2.75+(0.1*2.75))
    print("---------- Pedido Registrado -----------")


def mostrarPedidos(i):
    print("---- Detalle compra -----")
    print("* Nombre del cliente",detalleCompra[0][i])
    print("* Apellido del cliente",detalleCompra[1][i])
    print("* Télefono del cliente",detalleCompra[2][i])
    print("* Nombre de la policrush",detalleCompra[3][i])
    print("* Dependencia de la policrush",detalleCompra[4][i])
    print("* Celular de la policrush",detalleCompra[5][i])
    print("* Código del pedido",detalleCompra[6][i])
    print("* Pago final",detalleCompra[7][i])


def buscarPedido():
    codigo = int(input("Ingrese el código ")) # 5678
    
    if codigo in detalleCompra[6]:

        dato = detalleCompra[6].index(codigo) # 5678 2

        for i in range(len(detalleCompra[0])):
            
            if i == dato:
                mostrarPedidos(i)

    else:
        print("No existe ese pedido")



def main():
    print("----- Bienvenid@s-------")
    opcion= menuOpciones()
    while opcion !=4:
        if opcion ==1:
            ingresarPedidos()
            opcion= menuOpciones()
        elif opcion ==2:
            if len(detalleCompra[0]) ==0:
                print("No existen pedidos")
            else:
                for i in range(len(detalleCompra[0])):
                    mostrarPedidos(i)
            opcion= menuOpciones()
        elif opcion ==3:
            buscarPedido()
            opcion= menuOpciones()

    print("--- Muchas gracias ----")

main()