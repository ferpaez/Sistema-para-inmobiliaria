# date_1 = datetime.date.strptime("01/11/2023", "%d/%m/%Y") 
# [(date_1 + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(0,31)] # string
# #  [(date_1 + datetime.timedelta(days=i)) for i in range(0,31)] # objetos datetime
# #  [(date_1 + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(0,31)] # string
# # datetime.date.today() # dia actual

import csv
import datetime
from filtros import mostrar_propiedades
from administracion import limpiar_consola
from tabulate import tabulate

def citas():                                            #crea el archivo .csv para citas de todo un mes
    # Define la fecha de inicio
    fecha_inicio = datetime.date.today()
    # Define la fecha de finalización (un mes después)
    fecha_fin = fecha_inicio + datetime.timedelta(days=30)

    # Horarios disponibles
    horarios = ["09:00", "12:00", "15:00"]

    # Crea una lista para almacenar las citas programadas
    citas_programadas = []

    # Itera a través de las fechas y horarios
    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_fin:
        for horario in horarios:
            # Crea una fila para la cita
            cita = [fecha_actual.strftime("%d/%m/%Y"), horario, "", "", ""]
            citas_programadas.append(cita)
        fecha_actual += datetime.timedelta(days=1)

    # Escribe las citas programadas en el archivo CSV
    with open('citas.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(citas_programadas)

    print("Citas programadas con éxito.")
    print(citas_programadas)
    salida = input("Presione enter para salir.")

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
        citas_tabulate = []
        for row in reader:
            if row[2] == "":
                citas_tabulate.append([row[0], row[1]])
        print(tabulate(citas_tabulate, headers=["Fecha", "Horario"], tablefmt="fancy_grid"))

CITAS = 'citas.csv'



def agendar_cita():
    cita = int(input("¿Desea agendar una cita? 1- Sí, 2- No: "))

    if cita == 1:
        mostrar_citas_disponibles()
        print('-----------------------------')
        dia = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
        dia = dia.lower()
        horario = input("Ingrese el horario de la cita (hh:mm): ")

        with open(CITAS, 'r') as file:
            reader = csv.reader(file, delimiter=";")
            citas = list(reader)

        for i in citas:
            if dia == i[0] and horario == i[1] and i[2] == "":
                nombre = input("Ingrese su apellido y nombre: ")
                mail = input("Ingrese su mail: ")
                direccion = input("Ingrese la direccion que desea visitar: ")
                
                # direccuin = validador_direccion(visita)

                i[2] = nombre
                i[3] = mail
                i[4] = direccion

                with open('citas.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerows(citas)
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
        dia = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
        dia = dia
        horario = input("Ingrese el horario de la cita (hh:mm): ")
        with open('citas.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)
        for row in rows:
            if dia == row[0] and horario == row[1]:
                row[2] = ""
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
        citasagendadas_tabulate = []
        for row in reader:
            if row[2] != "":
                citasagendadas_tabulate.append([row[0], row[1], row[2], row[3], row[4]])
        print(tabulate(citasagendadas_tabulate, headers=["Fecha", "Horario", "Nombre", "Mail", "Direccion"], tablefmt="fancy_grid"))



def contador_visitas_propiedades():
    # Cargar las citas programadas
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        citas = list(reader)

    # Crear una lista para almacenar las visitas por propiedad
    visitas_por_propiedad = []

    # Cargar las propiedades
    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        propiedades = list(reader)

    # Inicializar la lista de visitas por propiedad
    for propiedad in propiedades:
        visitas_por_propiedad.append([propiedad[4], 0])  # Supongo que la dirección de la propiedad está en la columna 4

    # Contar las visitas por propiedad
    for cita in citas:
        if cita[2] != "":
            direccion = cita[4]  # Supongo que la dirección de la propiedad está en la columna 4
            for visita in visitas_por_propiedad:
                if visita[0] == direccion:
                    visita[1] += 1
                    break

    # Agregar las visitas a las propiedades
    for propiedad, visitas in zip(propiedades, visitas_por_propiedad):
        propiedad.append(visitas[1])

    # Ordenar las propiedades por barrio
    propiedades.sort(key=lambda propiedad: propiedad[1])

    # Crear un archivo CSV con los resultados
    with open('visitas.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(propiedades)

    print('---------------------------------------')
    print('Archivo de visitas creado exitosamente.')
    print('---------------------------------------')





# def agendar_cita():
#     cita = int(input("¿Desea agendar una cita? 1- Sí, 2- No: "))

#     if cita == 1:
#         mostrar_citas_disponibles()
#         print('-----------------------------')

#         # Nueva funcionalidad: Agregar fechas y horarios hasta un mes en el futuro
#         # fechas_horarios = generar_fechas_horarios()

#         # for fecha, horario in fechas_horarios:
#         #     if verificar_cita_programada(fecha, horario):
#         #         print(f'Cita ya agendada para {fecha} a las {horario}.')
#         dia = input("Ingrese el día de la cita: ")
#         dia = dia.lower()
#         horario = input("Ingrese el horario de la cita: ")
#         with open(CITAS, 'r') as file:
#             reader = csv.reader(file, delimiter=";")
#             disponibilidad = list(reader)

#         for row in disponibilidad:
#             if dia == row[0] and horario == row[1] and row[2] == "":
#                 nombre = input("Ingrese su apellido y nombre: ")
#                 mail = input("Ingrese su mail: ")
#                 visita = input("Ingrese la direccion que desea visitar: ")
                
#         else:
#                 nombre = input("Ingrese su apellido y nombre: ")
#                 mail = input("Ingrese su mail: ")
#                 visita = input("Ingrese la dirección que desea visitar: ")

#                 # Agrega la cita al archivo CSV
#                 with open(CITAS, 'a', newline='') as file:
#                     writer = csv.writer(file, delimiter=";")
#                     writer.writerow([nombre, fecha, horario, '', mail, visita])
#                     print('-----------------------------')
#                     print(f"Cita agendada exitosamente para {fecha} a las {horario}.")
#                     print('-----------------------------')
#     else:
#         print('-----------------------------')
#         print('Cita no agendada.')
#         print('-----------------------------')

# def verificar_cita_programada(fecha, horario):
#     with open(CITAS, 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         for row in reader:
#             cita_fecha = row[1]
#             cita_horario = row[2]
#             if cita_fecha == fecha and cita_horario == horario and row[0] != "":
#                 return True
#     return False

# def generar_fechas_horarios():
#     fechas_horarios = []
#     fecha_inicial = datetime.datetime.now()
#     for i in range(30):  # Generar citas para los próximos 30 días
#         fecha = fecha_inicial + datetime.timedelta(days=i)
#         for hora in range(8, 18, 2):  # Horarios desde las 8 AM hasta las 6 PM cada 2 horas
#             horario = f"{hora:02d}:00"
#             fechas_horarios.append((fecha.strftime("%d/%m/%Y"), horario))
#     return fechas_horarios

