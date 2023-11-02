#funciones citas
import csv
import os
from administracion import limpiar_consola

def agendar_cita():
    cita = int(input("¿Desea agendar una cita? 1- Sí, 2- No: "))

    if cita == 1:
        mostrar_citas_disponibles()
        print('-----------------------------')
        dia = input("Ingrese el día de la cita: ")
        dia = dia.lower()
        horario = input("Ingrese el horario de la cita: ")

        with open('citas.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)

        for row in rows:
            if dia == row[1] and horario == row[2] and row[0] == "":
                nombre = input("Ingrese su apellido y nombre: ")
                mail = input("Ingrese su mail: ")
                visita = input("Ingrese la direccion que desea visitar: ")

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
            print('-----------------------------')
            print("No hay citas disponibles para el día y horario especificados.")
            print('-----------------------------')

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
            print('-----------------------------')
            print("No hay citas agendadas para el día y horario especificados.")
            print('-----------------------------')

def ver_citas_agendadas():
    limpiar_consola()
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[0] != "":
                print (f"Nombre: {row[0]}, Día: {row[1]}, Horario: {row[2]}, Direccion: {row[5]}")

def mostrar_citas_disponibles():
    limpiar_consola()
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";") 
        for row in reader:
            if row[0] == "":
                print(f"Día: {row[1]}, Horario: {row[2]}")