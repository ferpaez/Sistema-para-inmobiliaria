import csv
from citas import agendar_cita, borrar_cita, ver_citas_agendadas, mostrar_citas_disponibles
from filtros import mostrar_propiedades, filtrar_por_barrio, filtrar_por_ambientes, filtrar_por_precio, menu_filtrado
from administracion import agregar_propiedad, quitar_propiedad
import os

# main menu

def main():
    while True:
        print('-----------------------------')
        print('Bienvenido al menú de gestión inmobiliaria')
        print('Ingrese 1 si desea agregar una propiedad')
        print('Ingrese 2 si desea buscar una propiedad')
        print('Ingrese 3 si desea agendar una cita')
        print('Ingrese 4 si desea ver citas agendadas')
        print('Ingrese 5 para borrar una cita')
        print('Ingrese 6 si desea eliminar una propiedad')
        print('Ingrese 0 para salir')
        print('-----------------------------')
        
        menu = int(input('Elija una opción: '))

        if menu == 0:
            break
        elif menu == 1:
            agregar_propiedad()
        elif menu == 2:
            menu_filtrado()
        elif menu == 3:
            agendar_cita()
        elif menu == 4:
            ver_citas_agendadas()
        elif menu == 5:
            borrar_cita()
        elif menu ==6:
            quitar_propiedad()
        else:
            print('-----------------------------')
            print('Opción no válida. Elija una opción del menú.')
            print('-----------------------------')
    print('-----------------------------')
    print('Gracias por usar el sistema de gestión inmobiliaria.')
    print('-----------------------------')

if __name__ == "__main__":
    main()
