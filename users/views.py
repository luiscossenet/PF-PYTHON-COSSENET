from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages

"""
from django.http import HttpResponse
from .models import *
from django.template import Template, Context, loader
from AppMagico.forms import *
from django.shortcuts import get_object_or_404
import requests
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from .forms import UserRegisterForm
from django.contrib.auth import logout
"""


# Create your views here.
#####################LOGIN ############################
def login_request(request):

    msg_login = ""
    userName = ""
    userMail = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=password)

            if user:
                # user is not None:

                login(request, user)
                userName = user.username
                userMail = user.email
                messages.success(request, f"Bienvenido {usuario}")
                return render(
                    request,
                    "AppMagico/index.html",
                    {"mensaje": f"Bienvenido {usuario}"},
                )

        msg_login = "Datos incorrectos"  # Si no pasó la validación de Django

    form = AuthenticationForm()
    return render(
        request,
        "users/login.html",
        {
            "form": form,
            "msg_login": msg_login,
            "user_name": userName,
            "user_mail": userMail,
        },
    )


#####################REGISTER ############################


# Vista de registro
def register(request):
    msg_register = ""
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            # usuario = form.cleaned_data.get("username")
            # *Prueba2024*
            # print(f"\nUsuario {username} Creado\n")
            messages.success(request, f"Usuario Creado {username}")
            return render(
                request,
                "AppMagico/index.html",
                {"mensaje": f"\nUsuario {username} Creado\n"},
            )

        msg_register = "Datos incorrectos"
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(
        request, "users/registro.html", {"form": form, "msg_register": msg_register}
    )


#####################LOGOUT ############################
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Añade un mensaje después de que el usuario cierra sesión
        messages.add_message(
            request, messages.SUCCESS, "Has cerrado sesión exitosamente."
        )
        return super().dispatch(request, *args, **kwargs)
