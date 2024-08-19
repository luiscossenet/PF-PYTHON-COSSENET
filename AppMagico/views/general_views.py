from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import UserProfile
from django.template import Template, Context, loader
from AppMagico.forms import *
from django.shortcuts import get_object_or_404
import requests
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def custom_404_view(request, exception):
    messages.error(request, "La página que estás buscando no existe. Has sido redirigido al inicio.")
    return redirect('inicio')  # 'index' es el nombre de la URL para la vista del índice

def custom_403_view(request, exception):
    #return render(request, '403.html', status=403)
    messages.error(request, "La página que estás intentando acceder, es una página o recurso para el cual no tienes los permisos necesarios. Has sido redirigido al inicio.")
    return redirect('inicio')  # 'index' es el nombre de la URL para la vista del índice

def custom_500_view(request):
    #return render(request, '500.html', status=500)
    messages.error(request, "La página que estás intentando acceder, presenta codigo #500. Has sido redirigido al inicio.")
    return redirect('inicio')  # 'index' es el nombre de la URL para la vista del índice

def custom_400_view(request, exception):
    #return render(request, '400.html', status=400)
    messages.error(request, "La página que estás intentando acceder, presenta codigo #400 *Solicitud incorrecta*, revisa los datos ingresados. Has sido redirigido al inicio.")
    return redirect('inicio')  # 'index' es el nombre de la URL para la vista del índice

def inicio(request):
    profile = UserProfile.objects.get(user=request.user)
    print(profile.profile_picture.url)
    return render(request, "index.html", {'profile_picture_url': profile.profile_picture.url})
    #return render(request, "index.html")


def ClubDeLectura(request):
    return render(request, "pages/clubdelectura.html")


def ClubDeRefuerzos(request):
    # return HttpResponse("Vista de inicio")
    return render(request, "pages/clubderefuerzos.html")


def ClubTallerIntegrado(request):
    # return HttpResponse("Vista de inicio")
    return render(request, "pages/clubtallerintegrado.html")


def ClubTardesMagicas(request):
    # return HttpResponse("Vista de inicio")
    return render(request, "pages/clubtardesmagicas.html")


def ClubTareasDirigidas(request):
    # return HttpResponse("Vista de inicio")
    return render(request, "pages/clubtareasdirigidas.html")


def Contactenos(request):
    # return HttpResponse("Vista de inicio")
    return render(request, "pages/contactenos.html")


def cursos(request):
    return HttpResponse("Vista de cursos")


def estudiantes(request):
    return HttpResponse("Vista de estudiantes")


def profesores(request):
    return HttpResponse("Vista de profesores")


def entregables(request):
    return HttpResponse("Vista de entregables")


def test(request):
    return render(request, "test.html")
