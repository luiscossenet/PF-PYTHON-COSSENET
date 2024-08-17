from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_picture']


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={
                # "class": "form-control",
                "placeholder": "Ingrese el Nombre de Usuario",
                "title": "*Presione ENVIAR / Ingrese el Nombre del Estado",
                "required": "required",
            }
        ),
        # help_text="Requerido",
    )
    email = forms.EmailField(
        label="Correo Electronico",
        widget=forms.TextInput(
            attrs={
                # "class": "form-control",
                "placeholder": "Ingrese el Correo Electronico",
                "title": "*Presione ENVIAR / Ingrese el Nombre del Estado",
                "required": "required",
            }
        ),
        # help_text="Requerido",
    )
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

        help_texts = {k: "" for k in fields}

        labels = {
            "username": "Nombre de usuario",
            "email": "Correo",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }


class UserRegisterFormAdm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
        help_texts = {k: "" for k in fields}
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
