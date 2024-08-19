from django.urls import path
from .views import general_views, profile_views
from .views.general_views import *
from .views.profile_views import *


# from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    # ruta de la pagina de inicio , funcion de la vista, nombre del objeto.
    path("", inicio, name="inicio"),
    path("pages/clubdelectura/", ClubDeLectura, name="ClubDeLectura"),
    path("pages/clubderefuerzos/", ClubDeRefuerzos, name="ClubDeRefuerzos"),
    path("pages/clubtallerintegrado/", ClubTallerIntegrado, name="ClubTallerIntegrado"),
    path("pages/clubtardesmagicas/", ClubTardesMagicas, name="ClubTardesMagicas"),
    path("pages/clubtareasdirigidas/", ClubTareasDirigidas, name="ClubTareasDirigidas"),
    path("pages/contactenos/", Contactenos, name="Contactenos"),
    path("pages/estadosAdd/", estadosViewAdd, name="RV_vEstadosAdd"),
    path("pages/estadosSelect/", estadosViewSelect, name="RV_vEstadosSelect"),
    path("pages/estadosSelectAll/", estadosViewSelectAll, name="RV_vEstadosSelectAll"),
    path("pages/estadosUpdate/", estadosViewUpdate, name="RV_vEstadosUpdate"),
    path(
        "pages/estadosUpdateRow/<int:id>/",
        estadosViewUpdateRow,
        name="RV_vEstadosUpdateRow",
    ),
    path(
        "pages/estadosUpdateRowCommit/",
        estadosViewUpdateRowCommit,
        name="RV_vEstadosUpdateRowCommit",
    ),
    path("pages/estadosDelete/", estadosViewDelete, name="RV_vEstadosDelete"),
    path(
        "pages/estadosDeleteRow/<int:id>/",
        estadosViewDeleteRow,
        name="RV_vEstadosDeleteRow",
    ),
    path(
        "pages/estadosDeleteRowCommit/",
        estadosViewDeleteRowCommit,
        name="RV_vEstadosDeleteRowCommit",
    ),
    # rutas de clases basadas en vistas
    path(
        "pages/cargosSelect/",
        CargosListView.as_view(),
        name="RV_vCargosSelect",
    ),
    path("pages/cargosAdd/", CargosCreateView.as_view(), name="RV_vCargosAdd"),
    path(
        "pages/cargosUpdate/",
        CargosUpdateView.as_view(),
        name="RV_vCargosUpdate",
    ),
    path(
        "pages/cargosUpdateRow/<int:pk>/update",
        CargosUpdateRowView.as_view(),
        name="RV_vCargosUpdateRow",
    ),
    path(
        "pages/cargosDelete/",
        CargosDeleteView.as_view(),
        name="RV_vCargosDelete",
    ),
    path(
        "pages/cargosDeleteRow/<int:pk>/delete",
        CargosDeleteRowView.as_view(),
        name="RV_vCargosDeleteRow",
    ),
    # FIN rutas de clases basadas en vistas
    path("pages/addTipoDocumento/", CrearTipoDocumento, name="RV_vCrearTipoDocumento"),
    path("pages/selTipoDocumento/", SelectTipoDocumento, name="RV_vSelTipoDocumento"),
    #path("test/", test, name="RV_vTest"),
    path("profile/", profile_views.ProfileView.as_view(), name="RV_vprofile"),
    path(
        "profile/function/",
        profile_views.profile_function_view,
        name="RV_profile_function",
    ),
]
