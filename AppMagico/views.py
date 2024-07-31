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
#clase magico
def crear_estado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_alta = request.POST['fecha_alta']
        estado = Estado(nombre=nombre, fecha_alta=fecha_alta)
        estado.save()
        return render(request, 'AppMagico/index.html')
    
    return render(request, 'AppMagico/curso_formulario.html')


# Clase 18
def curso(self):
    curso = Curso(nombre="Java", numero_curso=23801, descripcion ="Curso Java Completo",fecha_inicio ="2024-05-17",fecha_fin="2024-07-17")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} \nNumero de Curso: {curso.numero_curso} \nDescripcion: {curso.descripcion} \nFecha de Inicio: {curso.fecha_inicio} \nFecha de Fin: {curso.fecha_fin}"

    return HttpResponse(documentoDeTexto)

# Esta funcion crea un curso en la base de datos interactuando con el usuario
def crear_curso(self):
    nombre = input("Ingrese el nombre del curso: ")
    numero_curso = input("Ingrese el numero del curso: ")
    #Incluir try except para validar que el numero de curso sea un numero
    try:
        numero_curso = int(numero_curso)
    except:
        return HttpResponse("El numero de curso debe ser un numero entero")
    descripcion = input("Ingrese la descripcion del curso: ")
    fecha_inicio = input("Ingrese la fecha de inicio del curso: ")
    fecha_fin = input("Ingrese la fecha de fin del curso: ")

    curso = Curso(nombre=nombre, numero_curso=numero_curso, descripcion =descripcion,fecha_inicio =fecha_inicio,fecha_fin=fecha_fin)
    curso.save()
    documentoDeTexto = f"Curso Grabado: {curso.nombre} \nNumero de Curso: {curso.numero_curso} \nDescripcion: {curso.descripcion} \nFecha de Inicio: {curso.fecha_inicio} \nFecha de Fin: {curso.fecha_fin}"

    return HttpResponse(documentoDeTexto)


# Mostrar informacion
#cursos html
def mostrar_informacion(request):
    cursos = Curso.objects.all()
    documentoDeTexto = ""
    for curso in cursos:
        documentoDeTexto += f"Curso: {curso.nombre} \nNumero de Curso: {curso.numero_curso} \nDescripcion: {curso.descripcion} \nFecha de Inicio: {curso.fecha_inicio} \nFecha de Fin: {curso.fecha_fin}\n\n"

    ##return HttpResponse(documentoDeTexto)
    return render(request, 'cursos.html', {'cursos': cursos})


def libros(request):
    URL_API_BOOKS = "https://potterapi-fedeperin.vercel.app/es/books"
    response = requests.get(URL_API_BOOKS)
    print(response.status_code)
    libros = response.json()
    status_code = response.status_code
    return render(request, 'libros.html', {'libros': libros, 'status_code': status_code})
    #return render(request, 'libros.html', {'libros': libros})

    #postman para revisar api
    #thunder client extension de visual studio code

#Clase 21
def curso_formulario(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        numero_curso = request.POST['numero_curso']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']

        curso = Curso(nombre=nombre, numero_curso=numero_curso, descripcion =descripcion,fecha_inicio =fecha_inicio,fecha_fin=fecha_fin)
        curso.save()
        #return HttpResponse("Curso grabado")
        return render(request, 'AppCoder/index.html')
    
    return render(request, 'AppCoder/curso_formulario.html')

def probando_cargadores(request):
    nombre = "Python"
    apellido = "Django" 
    template = loader.get_template('template2.html')
    context = {'nombre': nombre, 'apellido': apellido}
    documento = template.render(context)
    return HttpResponse(documento)
#def form_con_api(request):
