import random, csv


def codigo_ID():
    ID=random.randint(100,9999)
    return ID


def registrar_pedido(lista):
    codigo=codigo_ID()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    comuna = input("Comuna: ")
    direccion=input("Direccion: ")
    disp10=int(input("Dispensador de 10 litros: "))
    disp15=int(input("Dispensador 15 litros: "))
    disp20=int(input("Dispensador 20 lts: "))

    usuario=[codigo, nombre, apellido, comuna, direccion, disp10, disp15, disp20]
    lista.append(usuario)
    return lista

def listar_pedidos(lista):
    for usuario in lista:
        lista_pedidos= (f"{codigo[0]} \t {nombre[1]}\t {apellido[2]} \t {comuna[3]} \t {direccion[4]} \t {disp10[5]} \t {disp15[6]} \t {disp20[7]}")
    return lista_pedidos


def hoja_ruta(lista_datos):
    with open ("planilla.csv", "w") as archivo:
        archivo=csv.writer(archivo)
        archivo.writerows("codigo", "nombre", "apellido", "comuna", "direccion", "disp10", "disp15", "disp20")
        for cliente in lista_datos:
            lista_datos = (f"{codigo[0]} \t {nombre[1]}\t {apellido[2]} \t {comuna[3]} \t {direccion[4]} \t {disp10[5]} \t {disp15[6]} \t {disp20[7]}")
        return archivo

