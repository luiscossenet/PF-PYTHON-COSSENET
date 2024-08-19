from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture','alternative_email', 'telephone' , 'cellphone'  ,'whatsapp','linkedin', 
                  'youtube' ,'instagram' ,'github', 'facebook', 'twitter','tiktok']

def edit_profile(request):
   
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'users/edit_profile.html', {'form': form})        


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
