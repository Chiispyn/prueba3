import funciones


lista_pedidos = []

while True:
    print("Bienvenido a CleanWasser")
    print("1: Registrar pedido")
    print("2: Listar todos los pedidos")
    print("3: imprimir una hoja de ruta")
    print("Buscar pedido por ID")
    print("5: Salir")
    opcion=int(input("Seleccione su opcion: "))
    if opcion==1:
        funciones.registrar_pedido(lista_pedidos)
    elif opcion==2:
        print(lista_pedidos)
    elif opcion==3:
        funciones.hoja_ruta(lista_pedidos)
    elif opcion ==4:
        print()
    elif opcion ==5:
        break
   