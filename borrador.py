#funciones citas
import csv
import os
from administracion import limpiar_consola
from filtros import mostrar_propiedades
from tabulate import tabulate

CITAS = 'citas.csv'
def agendar_cita():
    cita = int(input("¿Desea agendar una cita? 1- Sí, 2- No: "))

    if cita == 1:
        mostrar_citas_disponibles()
        print('-----------------------------')
        dia = input("Ingrese el día de la cita: ")
        dia = dia.lower()
        horario = input("Ingrese el horario de la cita: ")

        # while True:                                                                     #loop para validar la direccion
        #     visita = input("Ingrese la dirección que desea visitar: ")
        #     if validador_direccion(visita): 
        #         break
        #     else:
        #         print("La dirección ingresada no es válida. Por favor, ingrese una dirección válida.")

        with open(CITAS, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)

        for row in rows:
            if dia == row[1] and horario == row[2] and row[0] == "":
                nombre = input("Ingrese su apellido y nombre: ")
                mail = input("Ingrese su mail: ")
                visita = input("Ingrese la direccion que desea visitar: ")
                
                # direccuin = validador_direccion(visita)

                row[0] = nombre
                row[4] = mail
                row[5] = visita

                with open('citas.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerows(rows)
                    print('-----------------------------')
                    print("Cita agendada exitosamente.")
                    print('-----------------------------')
                    break
        else:
            print('----------------------------------------------------------------')
            print("No hay citas disponibles para el día y horario especificados.")
            print('----------------------------------------------------------------')

def borrar_cita():
    borrar_cita= int(input("¿Desea borrar una cita? 1- Sí, 2- No: "))
    if borrar_cita == 1:
        ver_citas_agendadas()
        dia = input("Ingrese el día de la cita: ")
        dia = dia.lower()
        horario = input("Ingrese el horario de la cita: ")
        with open('citas.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)
        for row in rows:
            if dia == row[1].lower() and horario == row[2]:
                row[0] = ""
                with open('citas.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerows(rows)
                    print('-----------------------------')
                    print("Cita borrada exitosamente.")
                    print('-----------------------------')
                    break
        else:
            print('----------------------------------------------------------------')
            print("No hay citas agendadas para el día y horario especificados.")
            print('----------------------------------------------------------------')

def ver_citas_agendadas():
    limpiar_consola()
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[0] != "":
                print (f"Nombre: {row[0]}, Día: {row[1]}, Horario: {row[2]}, Direccion: {row[5]}")

def mostrar_citas_disponibles():
    limpiar_consola()

    with open('propiedades.csv', 'r') as file:                        #muestra las propiedades para poder ver la direccion deseada para la cita
        reader = csv.reader(file, delimiter=";")                      #si el usuario filtro propiedades, muestra las propiedades filtradas
        lista_propiedades = list(reader)                              #sino muestra todas las propiedades disponibles
    with open('busquedafiltrada.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_filtrada = list(reader)
    if lista_filtrada != []:
        mostrar_propiedades(lista_filtrada)
    else:
        mostrar_propiedades(lista_propiedades)


    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";") 
        for row in reader:
            if row[0] == "":
                print(f"Día: {row[1]}, Horario: {row[2]}")

#funcion contador de visitas

def contador_visitas_propiedades():
    with open('propiedades.csv', 'r') as file:                      #importa a una lista las propiedades y las citas
        reader = csv.reader(file, delimiter=";")
        lista_propiedades = list(reader)
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_citas = list(reader)
    for propiedad in lista_propiedades:
        contador = 0
        for cita in lista_citas:
            if propiedad[2].lower() == cita[5].lower() and cita[0] != "":
                contador += 1
        propiedad.append(contador)
    lista_propiedades.sort(key=lambda propiedad: propiedad[1])
    with open('visitas.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(lista_propiedades)
    print('---------------------------------------')
    print('Archivo de visitas creado exitosamente.')
    print('---------------------------------------')
    for propiedad in lista_propiedades:
        if propiedad[7] != 0:
            print(f"BARRIO: {propiedad[1]}, DIRECCION: {propiedad[2]}, CANTIDAD DE VISITAS: {propiedad[7]}")    

#validadores

# def validador_direccion(visita):
        
#     direcciones_disponibles = []
#     with open('propiedades.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         propiedades_list = list(reader)

#         for row in propiedades_list:
#             visita = row[2] 
#             direcciones_disponibles.append(visita)

#     for _ in range(len(direcciones_disponibles)):
#         visita = input("Ingrese la dirección que desea visitar: ")
#         if visita in direcciones_disponibles:
#             return visita
#     print("La dirección ingresada no es válida. Por favor, ingrese una dirección válida.")
#     return None

#  import datetime 
#  date_1 = datetime.datetime.strptime("01/11/2023", "%d/%m/%Y") 
#  [(date_1 + datetime.timedelta(days=i)) for i in range(0,31)] # objetos datetime
#  [(date_1 + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(0,31)] # string
# datetime.date.today() # dia actual


# date_1 = datetime.date.strptime("01/11/2023", "%d/%m/%Y") 
# [(date_1 + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(0,31)] # string
# #  [(date_1 + datetime.timedelta(days=i)) for i in range(0,31)] # objetos datetime
# #  [(date_1 + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(0,31)] # string
# # datetime.date.today() # dia actual



# def contador_visitas_propiedades():
#     with open('citas.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         citas = list(reader)

#     visitas_por_propiedad = []

#     # Cargar las propiedades
#     with open('propiedades.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         propiedades = list(reader)

#     # Inicializar la lista de visitas por propiedad
#     for propiedad in propiedades:
#         visitas_por_propiedad.append([propiedad[4], 0])  # Supongo que la dirección de la propiedad está en la columna 4

#     # Contar las visitas por propiedad
#     for cita in citas:
#         if cita[2] != "":
#             direccion = cita[4]  # Supongo que la dirección de la propiedad está en la columna 4
#             for visita in visitas_por_propiedad:
#                 if visita[0] == direccion:
#                     visita[1] += 1
#                     break

#     # Agregar las visitas a las propiedades
#     for propiedad, visitas in zip(propiedades, visitas_por_propiedad):
#         propiedad.append(visitas[1])

#     # Ordenar las propiedades por barrio
#     propiedades.sort(key=lambda propiedad: propiedad[1])

#     # Crear un archivo CSV con los resultados
#     with open('visitas.csv', 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=";")
#         writer.writerows(propiedades)

#     print('---------------------------------------')
#     print('Archivo de visitas creado exitosamente.')
#     print('---------------------------------------')





# def generar_fechas_horarios():
#     fechas_horarios = []
#     fecha_inicial = datetime.datetime.now()
#     for i in range(30):  # Generar citas para los próximos 30 días
#         fecha = fecha_inicial + datetime.timedelta(days=i)
#         for hora in range(8, 18, 2):  # Horarios desde las 8 AM hasta las 6 PM cada 2 horas
#             horario = f"{hora:02d}:00"
#             fechas_horarios.append((fecha.strftime("%d/%m/%Y"), horario))
#     return fechas_horarios

