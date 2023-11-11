import csv
import os
from tabulate import tabulate

#funciones agregar y quitar propiedad

def agregar_propiedad():
    codigo = int(input('Ingrese el codigo de la propiedad: '))
    barrio = input('Ingrese el barrio: ')
    direccion = input('Ingrese la direccion: ')
    validador_direccion(direccion)
    ambientes = int(input('Ingrese la cantidad de ambientes: '))
    precio = int(input('Ingrese el precio: '))
    superficie = int(input('Ingrese la superficie: '))
    tipo = input('Ingrese el tipo de propiedad: ')

    with open('propiedades.csv', 'a', newline='') as file:                  #a es append, agrega al final del archivo. porque w sobreescribe todo el archivo
        writer = csv.writer(file, delimiter=";")
        writer.writerow([codigo, barrio, direccion, ambientes, precio, superficie, tipo])
    print('-----------------------------')
    print('Propiedad agregada con éxito')
    print('-----------------------------')

def quitar_propiedad():                                                                        
    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        rows = list(reader)
    lista_completa = []
    for row in rows:
        lista_completa.append(row)
    print(tabulate(lista_completa, headers=["Código", "Barrio", "Dirección", "Ambientes", "Precio", "Superficie", "Tipo"], tablefmt="fancy_grid"))
    direccion = input('Ingrese la direccion de la propiedad que desea eliminar: ')
    direccion = direccion.lower()
    for row in rows:
        if direccion == row[2].lower():
            rows.remove(row)
            with open('propiedades.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerows(rows)
                print('------------------------------------')
                print("Propiedad eliminada exitosamente.")
                print('------------------------------------')
                break
    else:
        print('-------------------------------------------')
        print("No se encontró la propiedad especificada.")
        print('-------------------------------------------')

#funcion para limpiar la pantalla

def limpiar_consola():
    sistema = os.name()
    if sistema == 'nt':                                 #si es windows devuelve nt, si es linux o mac devuelve posix
        os.system('cls') #en windows
    else:
        os.system('clear') #en linux/mac

#funcion para validar la direccion

def validador_direccion(direccion):                                 #funciona mas o menos, porque itera una sola vez
    with open('propiedades.csv', 'r') as file:                      #la lista de propiedades, y si ingresamos una direccion nueva
        reader = csv.reader(file, delimiter=";")                    #capaz ya la itero y no la encuentra
        lista_propiedades = list(reader)
    for i in lista_propiedades:
        while i[2].lower() == direccion.lower():
            print ("La dirección ya existe")
            direccion = input("Ingrese la dirección nuevamente: ")
    return True

