import csv
from citas import agendar_cita, borrar_cita, ver_citas_agendadas, mostrar_citas_disponibles, contador_visitas, citas, descargar_agenda
from filtros import mostrar_propiedades, filtrar_por_barrio, filtrar_por_ambientes, filtrar_por_precio, menu_filtrado, vaciar_busqueda_filtrada
from administracion import agregar_propiedad, quitar_propiedad, limpiar_consola
from tabulate import tabulate
import os

#pip install tabulate
#or
#pip3 install tabulate

# main menu

def main():
    while True:
        print('-------------------------------------------')
        print('Bienvenido al menú de gestión inmobiliaria')
        print('Ingrese 1 si desea agregar una propiedad')
        print('Ingrese 2 si desea eliminar una propiedad')
        print('Ingrese 3 si desea buscar una propiedad')
        print('Ingrese 4 si desea agendar una cita')
        print('Ingrese 5 si desea ver citas agendadas')
        print('Ingrese 6 para borrar una cita')
        print('Ingrese 7 para descargar la agenda por dia, semana o mes')
        print('Ingrese 8 para ver la cantidad de visitas por propiedad')
        print('Ingrese 9 para agregar un nuevo mes de agenda a partir de hoy')
        print('Ingrese 0 para salir')
        print('-------------------------------------------')
        
        menu = input('Elija una opción: ')

        if menu == '0':
            vaciar_busqueda_filtrada()           #vacía el archivo de búsqueda filtrada para que no se acumulen los resultados la proxima vez que se use el programa
            break
        elif menu == '1':
            agregar_propiedad()
        elif menu == '2':
            quitar_propiedad()
        elif menu == '3':
            menu_filtrado()
        elif menu == '4':
            agendar_cita()
        elif menu == '5':
            ver_citas_agendadas()
        elif menu == '6':
            borrar_cita()
        elif menu == '7':
            descargar_agenda()
        elif menu == '8':
            contador_visitas()
        elif menu == '9':
            citas()

        else:
            limpiar_consola()
            print('----------------------------------------------')
            print('Opción no válida. Elija una opción del menú.')
            print('----------------------------------------------')
    print('------------------------------------------------------')
    print('Gracias por usar el sistema de gestión inmobiliaria.')
    print('------------------------------------------------------')

if __name__ == "__main__":
    main()
