from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import *
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


# Create your views here.


def inicio(request):
    # cursos = Curso.objects.all()
    # return render(request, 'index.html', {'cursos': cursos})
    return render(request, "index.html")


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
