import csv
import datetime
from filtros import mostrar_propiedades
from administracion import limpiar_consola
from tabulate import tabulate
from validadores import validador_direccion_citas

def citas():                                #crea el archivo .csv para citas de todo un mes
    while True:
        contrasena = input('Ingrese la contraseña para iniciar un nuevo mes de citas: ') #contrasena admin123
        if contrasena == 'admin123':
            break
        else:
            print("La contraseña ingresada no es correcta, ingrese una contraseña valida.")
    
    limpiar_consola()
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
        for i in reader:
            if i[2] == "":
                citas_tabulate.append([i[0], i[1]])
        print(tabulate(citas_tabulate, headers=["Fecha", "Horario"], tablefmt="fancy_grid"))


def agendar_cita():
    
    while True:
        cita = input("¿Desea agendar una cita? 1- Sí, 2- No: ")
        if cita == '1' or cita == '2' or cita == 'si' or cita == 'no':
            break
        else:
            print("La opción ingresada no es valida. Por favor, ingrese una opción valida.")

    if cita == '1' or cita == 'si':
        mostrar_citas_disponibles()
        print('-----------------------------')
        dia = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
        horario = input("Ingrese el horario de la cita (hh:mm): ")
        with open('citas.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            citas = list(reader)

        for i in citas:
            if dia == i[0] and horario == i[1] and i[2] == "":
                while True:
                    nombre = input("Ingrese su apellido y nombre: ")                    #comprueba que el nombre no sea un numero
                    if nombre != "" and not nombre.isdigit():
                        break
                    else:
                        print("El formato de nombre ingresado no es valido. Por favor, ingrese un formato de nombre valido.")

                while True:
                    mail = input("Ingrese su mail: ")
                    if "@" in mail and mail.endswith(".com"):
                        break
                    else:
                        print("El mail ingresado no es valido. Por favor, ingrese un mail valido.")

                while True: 
                    direccion = input("Ingrese la direccion que desea visitar: ")
                    direccion = direccion.lower()
                    valida = validador_direccion_citas(direccion)
                    if valida != None:
                        break
                    else:
                        print("La dirección ingresada no es válida. Por favor, ingrese una dirección válida.")                

                i[2] = nombre
                i[3] = mail
                i[4] = direccion

                with open('citas.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerows(citas)
                    limpiar_consola()
                    print('-----------------------------')
                    print("Cita agendada exitosamente.")
                    print('-----------------------------')
                    break
        else:
            print('----------------------------------------------------------------')
            print("No hay citas disponibles para el día y horario especificados.")
            print('----------------------------------------------------------------')



def borrar_cita():

    while True:
        contrasena = input('Ingrese la contraseña para borrar una cita: ') #contrasena admin123
        if contrasena == 'admin123':
            break
        else:
            print("La contraseña ingresada no es correcta, ingrese una contraseña valida.")
    
    ver_citas_agendadas()
    dia = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
    horario = input("Ingrese el horario de la cita (hh:mm): ")
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        citas = list(reader)
    for row in citas:
        if dia == row[0] and horario == row[1]:
            row[2] = "" 
            row[3] = "" 
            row[4] = ""
            with open('citas.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerows(citas)
                limpiar_consola()
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


def descargar_agenda():
    limpiar_consola()
    while True:
        periodo = input('Descargar agenda del día, semana o mes (ingrese "dia", "semana" o "mes"): ')
        periodo = periodo.lower()
        if periodo in ['dia', 'semana', 'mes']:
            break
        else:
            print('Periodo de agenda no válido. Utilice "dia", "semana" o "mes".')
    
    with open('citas.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        citas = list(reader)

    citas_filtradas = []
    fecha_deseada = input('Ingrese la fecha deseada (dd/mm/yyyy): ')
    fecha_deseada = datetime.datetime.strptime(fecha_deseada, "%d/%m/%Y").date()

    if periodo == 'dia':
        for i in citas:
            cita_fecha = datetime.datetime.strptime(i[0], "%d/%m/%Y").date()
            if cita_fecha == fecha_deseada and i[2] != "":
                citas_filtradas.append(i)
    elif periodo == 'semana':                                                           #si se encuentra entre el dia ingresado y los seis dias posteriores lo agrega a la lista.
        for i in citas:
            cita_fecha = datetime.datetime.strptime(i[0], "%d/%m/%Y").date()
            if fecha_deseada <= cita_fecha <= fecha_deseada + datetime.timedelta(days=6) and i[2] != "":
                citas_filtradas.append(i)
    elif periodo == 'mes':
        for i in citas:
            cita_fecha = datetime.datetime.strptime(i[0], "%d/%m/%Y").date()
            if fecha_deseada.month == cita_fecha.month and i[2] != "":                          #si comparten el mes lo agrega a la lista
                citas_filtradas.append(i)

    nombre_archivo = f'agenda_{periodo}.csv'
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(citas_filtradas)

    limpiar_consola()
    print(tabulate(citas_filtradas, headers=["Fecha", "Horario", "Nombre", "Mail", "Direccion"], tablefmt="fancy_grid"))
    print(f'Archivo de agenda del {periodo} generado exitosamente: {nombre_archivo}')

