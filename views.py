import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#primera vista - forma indicada para renderizar una vista
def saludo(request):
    p = Persona('Daniel', 'Interiano')
    ahora = datetime.datetime.now()

    # creación del diccionario
    diccionario = {'nombres':p.nombre, 'apellidos':p.apellido, 'ahora': ahora,
                   'temas':['Plantillas','Modelos','Formularios','Vistas','Despliegues']}

    return render(request, "plantilla1.html", diccionario)

#segunda vista
def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')

#vistas dinámicas
def dame_fecha(request):
    fechaActual = datetime.datetime.now()
    documento = '''
        <body>
            <h1>Fecha y hora actual: %s</h1>
        </body>
    ''' % fechaActual
    return HttpResponse(documento)

#vista que calcula edad futura
def calcular_edad(request, edad, anio):
    periodo = anio - 2022
    edadFutura = edad + periodo
    documento = '''
        <body>
            <h2>En el año %s tendrás %s años</h2>
        </body>
    ''' % (anio, edadFutura)
    return HttpResponse(documento)
    