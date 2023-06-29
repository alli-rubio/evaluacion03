import numpy as np
from Libro import *
import random as rn

arreglo_libro = np.array([])
#random -> a = rn.randint(valormin, valormax)

def grabarLibro(arreglo_libro):
    lib = Libro()

    c = False
    while c == False:
        c = lib.setcodigo(input("Ingrese codigo en formato AAA-000:")) #no me acuerdoooooo
    lib.titulo = input("Ingrese titulo:")
    lib.autor = input("Ingrese autor:")
    c = False
    while c == False:
        try:
            c = lib.setprecio(int(input("Ingrese el precio entre 10000 y 150000:")))
        except BaseException as error:
            print(f"Error: {error}")
    c = False
    while c == False:
        try:
            c = lib.setfpub(int(input("Ingrese fecha de publicacion:")))
        except BaseException as error:
            print(f"Error: {error}")
    lib.pais = input("Ingrese el pais:")
    lib.categoria = input("Ingrese categoria:")
    print("Libro agregado con exito")

    return np.append(arreglo_libro,lib) #agregar al arreglo


def buscarLibro(arreglo_libro):
    codigo = input("Ingrese codigo en formato AAA-000:")
    flag = True
    for libro in arreglo_libro:
        if libro.codigo == codigo:
            flag = True
            print("Datos del libro")
            print(f"Titulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Categoria: {libro.categoria}")
            print(f"Pais:{libro.pais}")
            print(f"Precio: {libro.precio}")
            print(f"Codigo: {libro.codigo}")
            print(f"Fecha de publicacion: {libro.fpub}")
            if (2023 - libro.fpub) > 30:
                print("El libro es edicion especial")
            break
    if flag == False:
        print("El libro ingresado consultado no existe")


def imprimirPais(arreglo_libro):
    pais = input("Ingrese el país de origen:")
    nume = rn.randint(1500, 5000)
    flag = True
    total = 0
    for libro in arreglo_libro:
        if libro.pais == pais:
            flag = True
            print("Datos del libro")
            print("---------")
            print(f"Numero: {nume}")
            print(f"Listado por país")
            print(f"Titulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Categoria: {libro.categoria}")
            print(f"Publicacion: {libro.fpub}")
            b = libro.precio
            if (2023 - libro.fpub) > 5:
                b = (libro.precio * 0.85)
                print(f"Precio nuevo:{b}")
            total += b

    if flag == False:
        print("El libro ingresado consultado no existe")
    print(f"Total: {total}")

def imprimirCategoria(arreglo_libro):
    categoria = input("Ingrese la categoria:")
    nume = rn.randint(1500, 5000)
    flag = True
    total = 0
    for libro in arreglo_libro:
        if libro.categoria == categoria:
            flag = True
            print("Datos del libro")
            print("----------")
            print(f"Numero: {nume}")
            print(f"Listado por país")
            print(f"Titulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Categoria: {libro.categoria}")
            print(f"Publicacion: {libro.fpub}")
            print(f"Precio:{libro.precio}")
            x = libro.precio
            if (2023 - libro.fpub) > 5:
                x = (libro.precio * 0.85)
                print(f"Precio nuevo:{x}")
            total += x

    if flag == False:
        print("El libro ingresado consultado no existe")
    print(f"Total: {total}")

def imprimirLibro(arreglo_libro):
    print("1) Informes por pais")
    print("2) Informes por categoria")
    try:
        op_imp = int(input("Seleccione (1-2):"))
        match op_imp:
            case 1:
                imprimirPais(arreglo_libro)
            case 2:
                imprimirCategoria(arreglo_libro)
    except BaseException as error:
        print(f"Error: {error}")


def salir():
    print("Gracias por preferirnos")
    print("Allison Rubio Valenzuela, version 1.1")
    return False


ciclo = True

while ciclo:
    print("Libreria mayor")
    print("-----------------------")
    print("1) Grabar Libro")
    print("2) Buscar libro")
    print("3) Imprimir informes")
    print("4) Salir")

    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                arreglo_libro = grabarLibro(arreglo_libro)
            case 2:
                buscarLibro(arreglo_libro)
            case 3:
                imprimirLibro(arreglo_libro)
            case 4:
                ciclo = salir()
            case _:
                print("Opcion icorrecta")
    except BaseException as error:
        print(f"Error: {error}")