import csv


def validador_direccion_citas(direccion): 
    direcciones_disponibles = []

    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_propiedades = list(reader)

        #carga direcciones en lista
        for i in lista_propiedades:
            direccion2 = i[2].lower() 
            direcciones_disponibles.append(direccion2)
            
        #valida direccion
        if (direccion in direcciones_disponibles):
            print('La direccion es valida')
            return direccion
        else:
            return None
        
def validador_direccion_administracion(direccion):        
    direcciones_ingresadas= []

    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_propiedades = list(reader)

        #carga direcciones en lista
        for i in lista_propiedades:
            direccion2 = i[2].lower() 
            direcciones_ingresadas.append(direccion2)
            
        #valida direccion
        if (direccion  not in direcciones_ingresadas):
            print('La direccion es valida')
            return direccion
        else:
            return None                       

def validador_codigo(codigo):
    codigos = []

    with open('propiedades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        lista_codigos = list(reader)

        #carga codigos en lista
        for i in lista_codigos:
            codigo2 = i[0]
            codigos.append(codigo2)
            
        #valida codigo
        if (codigo not in codigos) and len(codigo) == 4 and codigo.isdigit():
            return codigo
        else:
            return None

