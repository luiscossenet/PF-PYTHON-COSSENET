from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages
import socket
from .models import UserProfile
from .utils import UserActivity

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'profile.html', {'profile': profile})

def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.updated_by = request.user
            user_activity = UserActivity(request)
            activity_data = user_activity.get_user_activity()
            profile.updated_ip_public = activity_data['ip_public']
            profile.updated_ip_local = activity_data['ip_local']
            profile.updated_host = activity_data['host_name']
            profile.updated_os = activity_data['os']
            profile.updated_browser = activity_data['browser']
            if 'profile_picture' in request.FILES:
                profile.profile_picture_original_name = request.FILES['profile_picture'].name
            profile.save()
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


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
