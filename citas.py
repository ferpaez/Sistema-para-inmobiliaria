import csv
import datetime
from filtros import mostrar_propiedades
from administracion import limpiar_consola
from tabulate import tabulate

def citas():                                #crea el archivo .csv para citas de todo un mes
    contrasena = input('Ingrese la contraseña para iniciar un nuevo mes de citas: ') #contrasena aguanteboca
    limpiar_consola()
    if contrasena == 'aguanteboca':
        fecha_inicio = datetime.date.today()
        fecha_fin = fecha_inicio + datetime.timedelta(days=30)
        horarios = ["09:00", "12:00", "15:00"]
        citas_programadas = []

        fecha_actual = fecha_inicio                         # Itera a través de las fechas y horarios
        while fecha_actual <= fecha_fin:
            for horario in horarios:
                cita = [fecha_actual.strftime("%d/%m/%Y"), horario, "", "", ""]
                citas_programadas.append(cita)
            fecha_actual += datetime.timedelta(days=1)

        
        with open('citas.csv', 'r') as file:                 
            reader = csv.reader(file, delimiter=";")               
            citas = list(reader)
            
        fechas_existentes = []                                  #guardo las fechas existentes en una lista para despues comprar con citas_faltantes, esto para que cuando hago .append no se repitan las fechas
        for i in citas:
            fechas_existentes.append(i[0])

        citas_faltantes = []
        for cita in citas_programadas:
            if cita[0] not in fechas_existentes:
                citas_faltantes.append(cita)



        with open('citas.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(citas_faltantes)
        
        # with open('citas.csv', 'r') as file:
        #     reader = csv.reader(file, delimiter=";")
        #     citas = list(reader)

        # fechas_existentes = []                    #guarda las fechas existentes en una lista para despues comparar con citas_faltantes
        # for i in citas:                           #para que cuando hace .append no se repitan las fechas
        #     fechas_existentes.append(i[0])

        # citas_faltantes = []
        # for i in citas_programadas:
        #     if cita[0] not in fechas_existentes:
        #         citas_faltantes.append(cita)        

        # with open('citas.csv', 'a', newline='') as file:
        #     writer = csv.writer(file, delimiter=";")
        #     writer.writerows(citas_faltantes)

        print("Citas programadas con éxito.")

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


def agendar_cita():
    cita = int(input("¿Desea agendar una cita? 1- Sí, 2- No: "))

    if cita == 1:
        mostrar_citas_disponibles()
        print('-----------------------------')
        dia = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
        dia = dia.lower()
        horario = input("Ingrese el horario de la cita (hh:mm): ")

        with open('citas.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            citas = list(reader)

        for i in citas:
            if dia == i[0] and horario == i[1] and i[2] == "":
                nombre = input("Ingrese su apellido y nombre: ")
                mail = input("Ingrese su mail: ")
                direccion = input("Ingrese la direccion que desea visitar: ")
                
                # direccion = validador_direccion(direccion)

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

def contador_visitas():
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        citas = list(reader)

    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        propiedades = list(reader)
    
    visitas_por_propiedad = {}

    fecha_actual= datetime.date.today().strftime("%d/%m/%Y")                #paso la fecha actual a str con strftime
    for i in citas:
        if i[0] <= fecha_actual and i[2] != "":
            direccion_propiedad = i[4].lower()  
            if direccion_propiedad in visitas_por_propiedad:                #cuenta las visitas por propiedad y las acumula en el diccionario
                visitas_por_propiedad[direccion_propiedad] += 1
            else:
                visitas_por_propiedad[direccion_propiedad] = 1
    
    for propiedad in propiedades:                                     # Actualiza las propiedades con la cantidad de visitas guardadas en el diccionario
        direccion = propiedad[2].lower()  
        if direccion in visitas_por_propiedad:
            propiedad.append(visitas_por_propiedad[direccion])
        else:
            propiedad.append(0)  

    propiedades.sort(key=lambda propiedad: propiedad[1])            # Ordena las propiedades por barrio con la funcion lambda

    with open('visitas.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(propiedades)

    print(tabulate(propiedades, headers=["Código", "Barrio", "Dirección", "Ambientes", "Precio", "Superficie", "Tipo", "Visitas"], tablefmt="fancy_grid"))
    print('---------------------------------------')
    print('Archivo de visitas creado exitosamente.')
    print('---------------------------------------')

# def validador_visita(direccion):
        
#     direcciones_disponibles = []
#     with open('propiedades.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         propiedades_list = list(reader)

#         for i in propiedades_list:
#             direccion = i[2].lower() 
#             direcciones_disponibles.append(direccion)

#         direccion = input("Ingrese la dirección que desea visitar: ")
#         for _ in range(len(direcciones_disponibles)):
#             if direccion in direcciones_disponibles:
#                 print('La direccion es valida')
#                 return direccion
#             else:
#                 print("La dirección ingresada no es válida. Por favor, ingrese una dirección válida.")


def descargar_agenda():
    periodo = input('Descargar agenda del día, semana o mes (ingrese "dia", "semana" o "mes"): ')
    periodo = periodo.lower()
    if periodo not in ['dia', 'semana', 'mes']:
        print('Periodo de agenda no válido. Utilice "dia", "semana" o "mes".')
        return
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        citas = list(reader)

    citas_filtradas = []
    fecha_deseada = input('Ingrese la fecha deseada (dd/mm/yyyy): ')
    fecha_deseada = datetime.datetime.strptime(fecha_deseada, "%d/%m/%Y").date()
    for i in citas:
        fecha_cita = datetime.datetime.strptime(i[0], "%d/%m/%Y").date()
        if fecha_cita == fecha_deseada and periodo == 'dia' and i[2] != "":
            citas_filtradas.append(i)
        elif fecha_cita == fecha_deseada and periodo == 'semana':
            for _ in range(7):                                                           # Itera a través de los 7 días de la semana
                for i in citas:
                    if i[0] == fecha_deseada.strftime("%d/%m/%Y") and i[2] != "":        # Itera para chequear los tres horarios del dia y verifica si la cita esta ocupada
                        citas_filtradas.append(i)
                fecha_deseada = fecha_deseada + datetime.timedelta(days=i)
        elif fecha_cita == fecha_deseada and periodo == 'mes':
            for _ in range(30):                                                           
                for i in citas:
                    if i[0] == fecha_deseada.strftime("%d/%m/%Y") and i[2] != "":      
                        citas_filtradas.append(i)
                fecha_deseada = fecha_deseada + datetime.timedelta(days=1)

    nombre_archivo = f'agenda_{periodo}.csv'
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(citas_filtradas)

    limpiar_consola()
    print(tabulate(citas_filtradas, headers=["Fecha", "Horario", "Nombre", "Mail", "Direccion"], tablefmt="fancy_grid"))
    print(f'Archivo de agenda del {periodo} generado exitosamente: {nombre_archivo}')
