import datetime

from django.http import HttpResponse
from django.template import Context, Template
from django.templete.loader import get_template


#primera vista
def saludo(request):
    nombre = 'Daniel Stanly'
    apellido = 'Interiano Rápalo'
    ahora = datetime.datetime.now()

    # variable que permite cargar cualquier template
    doc_externo = get_template('plantilla1.html')

    # creación del contexto
    diccionario = {'nombres':nombre, 'apellidos':apellido, 'ahora': ahora,
                   'temas':['Plantillas','Modelos','Formularios','Vistas','Despliegues']}

    # creación de documento a renderizar
    documento = doc_externo.render(diccionario)

    return HttpResponse(documento)

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
    