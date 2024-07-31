from django.shortcuts import render
from django.http import HttpResponse   
from .models import * 
from django.template import Template, Context, loader
import requests

# Create your views here.


def inicio(request):
    #cursos = Curso.objects.all()
    #return render(request, 'index.html', {'cursos': cursos})
    return render(request, 'index.html')

def ClubDeLectura(request):
    return render(request, 'pages/clubdelectura.html')

def ClubDeRefuerzos(request):
    #return HttpResponse("Vista de inicio")
    return render(request, 'pages/clubderefuerzos.html')

def ClubTallerIntegrado(request):
    #return HttpResponse("Vista de inicio")
    return render(request, 'pages/clubtallerintegrado.html')

def ClubTardesMagicas(request):
    #return HttpResponse("Vista de inicio")
    return render(request, 'pages/clubtardesmagicas.html')

def ClubTareasDirigidas(request):
    #return HttpResponse("Vista de inicio")
    return render(request, 'pages/clubtareasdirigidas.html')

def Contactenos(request):
    #return HttpResponse("Vista de inicio")
    return render(request, 'pages/contactenos.html')

def cursos(request):
    return HttpResponse("Vista de cursos")

def estudiantes(request):
    return HttpResponse("Vista de estudiantes")

def profesores(request):
    return HttpResponse("Vista de profesores")  

def entregables(request):    
    return HttpResponse("Vista de entregables") 


# CRUD operations for each model
def CrearEstado(request):
    if request.method == 'POST':
        idEstado = request.POST['codigoEstado']
        nombreEstado = request.POST['nombreEstado']
        fechaAlta = request.POST['fechaRegistro']
        estado = Estado(id_estado=idEstado, nombre=nombreEstado, fecha_alta=fechaAlta)
        try:
            estado.save()
            mensaje = f"Estado: {nombreEstado} con codigo: {idEstado} y fecha de registro: {fechaAlta}"
            statuscode = 200
            print("Estado grabado")
        except:
            mensaje = "El registro ya existe"
            statuscode = 200
            print("El registro ya existe")
        print( {'mensaje': mensaje, 'status_code': statuscode})
            #mensaje = "Estado grabado exitosamente"
        return render(request, 'pages/addEstados.html', {'mensaje': mensaje})
    
    
    return render(request, 'pages/addEstados.html')

# CRUD operations for each model
def SelectEstado(request):
    if request.method == 'POST':
        valorConsultado = request.POST['valorConsulta']
        resultadoConsulta = Estado.objects.filter(nombre__icontains=valorConsultado)
        context = {
        'mensaje': resultadoConsulta,
        'statuscode':200,
        'respuesta': 'Estado consultado'
        }
        return render(request, 'pages/selEstados.html', context)
    
    
    return render(request, 'pages/selEstados.html')


#####################TipoDocumento
# CRUD operations for each model
def CrearTipoDocumento(request):
    if request.method == 'POST':
        codigoDocumento = request.POST['codigo_documento']
        nombreEstado = request.POST['nombre']
        idEstado = request.POST['id_estado']
        usuarioAlta = request.POST['usuario_alta']
        fechaAlta = request.POST['fecha_alta']
        estado = Estado(codigo_documento=codigoDocumento, nombre=nombreEstado, id_estado=idEstado,usuario_alta=usuarioAlta, fecha_alta=fechaAlta)
        try:
            estado.save()
            mensaje = f"Estado: {nombreEstado} con codigo: {codigoDocumento} y fecha de registro: {fechaAlta}"
            statuscode = 200
            print("Estado grabado")
        except:
            mensaje = "El registro ya existe"
            statuscode = 200
            print("El registro ya existe")
        print( {'mensaje': mensaje, 'status_code': statuscode})
            #mensaje = "Estado grabado exitosamente"
        return render(request, 'pages/addTipoDocumento.html', {'mensaje': mensaje})
    
    
    return render(request, 'pages/addEstados.html')

# CRUD operations for each model
def SelectTipoDocumento(request):
    if request.method == 'POST':
        valorConsultado = request.POST['valorConsulta']
        resultadoConsulta = Estado.objects.filter(nombre__icontains=valorConsultado)
        context = {
        'mensaje': resultadoConsulta,
        'statuscode':200,
        'respuesta': 'Estado consultado'
        }
        return render(request, 'pages/selEstados.html', context)
    
    
    return render(request, 'pages/selEstados.html')

############CrearCargos

# CRUD operations for each model
def CrearCargos(request):
    if request.method == 'POST':
        idEstado = request.POST['codigoEstado']
        nombreEstado = request.POST['nombreEstado']
        fechaAlta = request.POST['fechaRegistro']
        estado = Estado(id_estado=idEstado, nombre=nombreEstado, fecha_alta=fechaAlta)
        try:
            estado.save()
            mensaje = f"Estado: {nombreEstado} con codigo: {idEstado} y fecha de registro: {fechaAlta}"
            statuscode = 200
            print("Estado grabado")
        except:
            mensaje = "El registro ya existe"
            statuscode = 200
            print("El registro ya existe")
        print( {'mensaje': mensaje, 'status_code': statuscode})
            #mensaje = "Estado grabado exitosamente"
        return render(request, 'pages/addEstados.html', {'mensaje': mensaje})
    
    
    return render(request, 'pages/addEstados.html')

# CRUD operations for each model
def SelectCargos(request):
    if request.method == 'POST':
        valorConsultado = request.POST['valorConsulta']
        resultadoConsulta = Estado.objects.filter(nombre__icontains=valorConsultado)
        context = {
        'mensaje': resultadoConsulta,
        'statuscode':200,
        'respuesta': 'Estado consultado'
        }
        return render(request, 'pages/selEstados.html', context)
    
    
    return render(request, 'pages/selEstados.html')

