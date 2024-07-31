from django.urls import path
from AppMagico.views import *

urlpatterns = [
    # ruta de la pagina de inicio , funcion de la vista, nombre del objeto
    path('', inicio,name='inicio'),
    path('pages/clubdelectura/', ClubDeLectura,name='ClubDeLectura'),
    path('pages/clubderefuerzos/', ClubDeRefuerzos,name='ClubDeRefuerzos'),
    path('pages/clubtallerintegrado/', ClubTallerIntegrado,name='ClubTallerIntegrado'),
    path('pages/clubtardesmagicas/', ClubTardesMagicas,name='ClubTardesMagicas'),
    path('pages/clubtareasdirigidas/', ClubTareasDirigidas,name='ClubTareasDirigidas'),
    path('pages/contactenos/', Contactenos,name='Contactenos'),    
    path('pages-cursos/', cursos,name='cursos'),
    path('pages-estudiantes/', estudiantes),
    path('pages-profesores/', profesores),
    path('pages-entregables/', entregables),
    path('libros/', libros),
    path('cargadores/', probando_cargadores),
    #-------------#
    path('curso/', curso),
    path('crearcurso/', crear_curso),
    path('mostrarinformacion/', mostrar_informacion, name='mostrarCursos'),
    
]

clase_21 = [
    #ruta de la clase 21
    path('clase21/', curso_formulario),
    
]

urlpatterns = urlpatterns + clase_21