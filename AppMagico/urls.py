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
    path('pages/addEstados/', CrearEstado,name='CrearEstado'),  
    path('pages/selEstados/', SelectEstado,name='SelEstado'),
    path('pages/addTipoDocumento/', CrearTipoDocumento,name='CrearTipoDocumento'),  
    path('pages/selTipoDocumento/', SelectTipoDocumento,name='SelTipoDocumento'),      
    path('pages/addCargos/', CrearCargos,name='CrearCargos'),  
    path('pages/selCargos/', SelectCargos,name='SelCargos'),       
]