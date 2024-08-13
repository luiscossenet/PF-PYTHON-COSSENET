from django.urls import path
from AppMagico.views import *

urlpatterns = [
    # ruta de la pagina de inicio , funcion de la vista, nombre del objeto.
    path("", inicio, name="inicio"),
    path("pages/clubdelectura/", ClubDeLectura, name="ClubDeLectura"),
    path("pages/clubderefuerzos/", ClubDeRefuerzos, name="ClubDeRefuerzos"),
    path("pages/clubtallerintegrado/", ClubTallerIntegrado, name="ClubTallerIntegrado"),
    path("pages/clubtardesmagicas/", ClubTardesMagicas, name="ClubTardesMagicas"),
    path("pages/clubtareasdirigidas/", ClubTareasDirigidas, name="ClubTareasDirigidas"),
    path("pages/contactenos/", Contactenos, name="Contactenos"),
    path("pages/estadosAdd/", estadosViewAdd, name="vEstadosAdd"),
    path("pages/estadosSelect/", estadosViewSelect, name="vEstadosSelect"),
    path("pages/estadosSelectAll/", estadosViewSelectAll, name="vEstadosSelectAll"),
    path("pages/estadosUpdate/", estadosViewUpdate, name="vEstadosUpdate"),
    path(
        "pages/estadosUpdateRow/<int:id>/",
        estadosViewUpdateRow,
        name="vEstadosUpdateRow",
    ),
    path(
        "pages/estadosUpdateRowCommit/",
        estadosViewUpdateRowCommit,
        name="vEstadosUpdateRowCommit",
    ),
    path("pages/estadosDelete/", estadosViewDelete, name="vEstadosDelete"),
    path(
        "pages/estadosDeleteRow/<int:id>/",
        estadosViewDeleteRow,
        name="vEstadosDeleteRow",
    ),
    path(
        "pages/estadosDeleteRowCommit/",
        estadosViewDeleteRowCommit,
        name="vEstadosDeleteRowCommit",
    ),
    path("pages/addTipoDocumento/", CrearTipoDocumento, name="CrearTipoDocumento"),
    path("pages/selTipoDocumento/", SelectTipoDocumento, name="SelTipoDocumento"),
    path("pages/addCargos/", CrearCargos, name="CrearCargos"),
    path("pages/selCargos/", SelectCargos, name="SelCargos"),
    path("pages/cursoFormul/", cursoFormulario, name="CursoFormulario"),
]
