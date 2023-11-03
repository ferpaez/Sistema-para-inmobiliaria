import csv
import os
from administracion import limpiar_consola
from tabulate import tabulate

#funciones filtros

def mostrar_propiedades(lista_propiedades):
    limpiar_consola()
    resultado = []
    for propiedad in lista_propiedades:
        resultado.append(propiedad)
    print(tabulate(resultado, headers=["Código", "Barrio", "Dirección", "Ambientes", "Precio", "Superficie", "Tipo"], tablefmt="fancy_grid"))

def filtrar_por_barrio(lista_propiedades, barrio):
    return [propiedad for propiedad in lista_propiedades if propiedad[1] == barrio]

def filtrar_por_ambientes(lista_propiedades, ambientes):
    return [propiedad for propiedad in lista_propiedades if propiedad[3] == ambientes]

def filtrar_por_precio(lista_propiedades, preciomin, preciomax):
    return [propiedad for propiedad in lista_propiedades if preciomin <= int(propiedad[4]) <= preciomax]

def menu_filtrado():
    filtros = []
    tipodepropiedad = input('¿Está buscando un departamento o una casa? ')
    tipodepropiedad = tipodepropiedad.lower()

    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_propiedades = list(reader)                                                                              #crea una lista de listas del archivo csv

    if tipodepropiedad == "casa" or tipodepropiedad == "departamento":
        propiedades_filtradas = [propiedad for propiedad in lista_propiedades if propiedad[6] == tipodepropiedad]

        print(f'Las {tipodepropiedad}s disponibles son:')
        mostrar_propiedades(propiedades_filtradas)

        eleccion = None
        while eleccion != '0':
            print('-----------------------------------------------------------------------')
            print('Desea agregar un filtro?')
            print('Ingrese 1 para filtrar por barrio')
            print('Ingrese 2 para filtrar por cantidad de ambientes')
            print('Ingrese 3 para filtrar por precio')
            print('Ingrese 0 para ver los resultados')
            print('-----------------------------------------------------------------------')
            eleccion = input('Elija una opción: ')

            if eleccion == '1':
                barrio = input('Ingrese el barrio: ')
                barrio = barrio.lower()
                propiedades_filtradas = filtrar_por_barrio(propiedades_filtradas, barrio)
                mostrar_propiedades(propiedades_filtradas)
            elif eleccion == '2':
                ambientes = input('Ingrese la cantidad de ambientes: ')
                propiedades_filtradas = filtrar_por_ambientes(propiedades_filtradas, ambientes)
                mostrar_propiedades(propiedades_filtradas)
            elif eleccion == '3':
                preciomin = int(input('Ingrese un precio mínimo deseado:'))
                preciomax = int(input('Ingrese un precio máximo deseado:'))
                propiedades_filtradas = filtrar_por_precio(propiedades_filtradas, preciomin, preciomax)
                mostrar_propiedades(propiedades_filtradas)

        filtros.extend(propiedades_filtradas)

    if filtros:
        print('Resultados:')
        mostrar_propiedades(filtros)
        escritorcsv(filtros)
    else:
        print('-------------------------------------------------------------------------')
        print('No se encontraron propiedades que cumplan con los filtros seleccionados.')
        print('-------------------------------------------------------------------------')

#funcion para crear un archivo con los resultados de la busqueda

def escritorcsv(filtros):
    archivo = input('Desea guardar los resultados de su búsqueda en un archivo? 1- Sí, 2- No:')
    if archivo == '1':
        with open('busquedafiltrada.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(filtros)
            print('-----------------------------------------------------------')
            print('Se ha creado un archivo con los resultados de su búsqueda.')
            print('-----------------------------------------------------------')
    else:
        print('-----------------------------------------------------------')
        print('No se ha creado un archivo con los resultados de su búsqueda.')
        print('-----------------------------------------------------------')

def vaciar_busqueda_filtrada():
    with open('busquedafiltrada.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows([])