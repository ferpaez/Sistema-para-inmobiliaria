import csv
import os
from tabulate import tabulate
from validadores import validador_direccion_administracion, validador_codigo

#funciones agregar y quitar propiedad

def agregar_propiedad():

    while True:
        codigo = input('Ingrese un codigo de cuatro digitos para la propiedad: ')
        valida = validador_codigo(codigo)
        if valida != None:
            break
        else:
            limpiar_consola()
            print("El codigo ingresado no es valido. Por favor, ingrese un código valido.")
    
    while True:
        barrio = input('Ingrese el barrio: ')
        barrio = barrio.lower()
        if barrio.isalpha():
            break
        else:
            limpiar_consola()
            print("El barrio ingresado no es valido. Por favor, ingrese un barrio valido.")
    
    while True: 
        direccion = input("Ingrese la direccion que desea agregar: ")
        valida = validador_direccion_administracion(direccion)
        if valida != None:
            break
        else:
            limpiar_consola()
            print("La dirección ingresada no es valida. Por favor, ingrese una dirección valida.")

    while True:
        ambientes = input('Ingrese la cantidad de ambientes: ')
        if ambientes.isdigit():
            break
        else:
            limpiar_consola()
            print("La cantidad de ambientes ingresada no es valida. Por favor, ingrese una cantidad valida.")

    while True:
        precio = input('Ingrese el precio: ')
        if precio.isdigit():
            break
        else:
            limpiar_consola()
            print("El precio ingresado no es valido. Por favor, ingrese un precio valido.")

    while True:
        superficie = input('Ingrese la superficie: ')
        if superficie.isdigit():
            break
        else:
            limpiar_consola()
            print("La superficie ingresada no es valida. Por favor, ingrese una superficie valida.")
    
    while True:
        tipo = input('Ingrese el tipo de propiedad: ')
        if tipo == 'casa' or tipo == 'departamento':
            break
        else:
            limpiar_consola()
            print("El tipo ingresado no es valido. Por favor, ingrese un tipo valido.")

    with open('propiedades.csv', 'a', newline='') as file:                 
        writer = csv.writer(file, delimiter=";")
        writer.writerow([codigo, barrio, direccion, ambientes, precio, superficie, tipo])
    
    limpiar_consola()
    print('-----------------------------')
    print('Propiedad agregada con éxito')
    print('-----------------------------')

def quitar_propiedad():                                                                        
    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        propiedades = list(reader)
    lista_completa = []
    for i in propiedades:
        lista_completa.append(i)
    print(tabulate(lista_completa, headers=["Código", "Barrio", "Dirección", "Ambientes", "Precio", "Superficie", "Tipo"], tablefmt="fancy_grid"))
    direccion = input('Ingrese la direccion de la propiedad que desea eliminar: ')
    direccion = direccion.lower()
    for i in propiedades:
        if direccion == i[2].lower():
            propiedades.remove(i)
            with open('propiedades.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerows(propiedades)
                print('------------------------------------')
                print("Propiedad eliminada exitosamente.")
                print('------------------------------------')
                break
    else:
        limpiar_consola()
        print('-------------------------------------------')
        print("No se encontró la propiedad especificada.")
        print('-------------------------------------------')

#funcion para limpiar la pantalla

def limpiar_consola():
    sistema = os.name
    if sistema == 'nt':                                 #si es windows devuelve nt, si es linux o mac devuelve posix
        os.system('cls') #en windows
    else:
        os.system('clear') #en linux/mac





