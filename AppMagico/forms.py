from django import forms
from .models import Estado, Empresa, Cargos, Usuarios, Tipo_Documento
from django.contrib.auth.models import User
import datetime


class EstadoForm(forms.Form):
    codigoEstado = forms.CharField(
        label="Codigo Estado",
        max_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Codigo del Estado",
            }
        ),
    )
    nombreEstado = forms.CharField(
        label="Nombre Estado",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Nombre del Estado",
            }
        ),
    )
    fechaRegistro = forms.DateField(
        label="Fecha de Registro",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        input_formats=["%Y-%m-%d"],
    )


class EstadoSelectForm(forms.Form):
    nombreEstado = forms.CharField(
        label="Nombre Estado",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Nombre del Estado",
            }
        ),
    )


class EstadoSelectAllForm(forms.Form):
    nombreEstado = forms.CharField(
        label="Nombre Estado",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "*Ingrese el Nombre del Estado",
                "data-toggle": "tooltip",
                "title": "*Presione ENVIAR / Ingrese el Nombre del Estado",
            }
        ),
    )


class EstadoUpdForm(forms.Form):
    # model = Estado
    id = forms.IntegerField(
        label="ID",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el ID",
                "readonly": "readonly",
            }
        ),
        required=False,
    )
    codigoEstado = forms.CharField(
        label="Codigo Estado",
        max_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Codigo del Estado",
                "readonly": "readonly",
            }
        ),
    )
    nombreEstado = forms.CharField(
        label="Nombre Estado",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Nombre del Estado",
            }
        ),
    )
    fechaRegistro = forms.DateField(
        label="Fecha de Registro",
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "readonly": "readonly",
            }
        ),
        input_formats=["%Y-%m-%d"],
    )


class EstadoDelForm(forms.Form):
    # model = Estado
    id = forms.IntegerField(
        label="ID",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el ID",
                "readonly": "readonly",
            }
        ),
        required=False,
    )
    codigoEstado = forms.CharField(
        label="Codigo Estado",
        max_length=1,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Codigo del Estado",
                "readonly": "readonly",
            }
        ),
    )
    nombreEstado = forms.CharField(
        label="Nombre Estado",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el Nombre del Estado",
                "readonly": "readonly",
            }
        ),
    )
    fechaRegistro = forms.DateField(
        label="Fecha de Registro",
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "readonly": "readonly",
            }
        ),
        input_formats=["%Y-%m-%d"],
    )


class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = [
            "nombre",
            "id_empresa",
            "id_estado",
            "usuario_alta",
            "fecha_alta",
        ]

    nombre = forms.CharField(
        label="Nombre",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese el Nombre del Cargo",
                "style": "width: 500px;",  # Set the width of the input field
                "oninput": "this.value = this.value.toUpperCase()",  # Convert input to uppercase
            }
        ),
    )
    fecha_alta = forms.DateField(
        label="Fecha de Alta",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "value": datetime.date.today().strftime("%Y-%m-%d"),
                "style": "width: 500px;",  # Set the width of the input field
            }
        ),
        input_formats=["%Y-%m-%d"],
        initial=datetime.date.today(),
    )

    id_empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(
            attrs={
                "style": "width: 500px;",
            }
        ),
        label="Empresa",
        empty_label="Seleccione una empresa",
    )

    id_estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        widget=forms.Select(
            attrs={
                "style": "width: 500px;",
            }
        ),
        label="Estado ",
        empty_label="Seleccione un estado",
    )

    usuario_alta = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Usuario Alta",
        widget=forms.Select(
            attrs={
                "placeholder": "Ingrese el Usuario de Alta",
                "style": "width: 500px;",  # Set the width of the input field
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar la etiqueta que se muestra para cada empresa
        self.fields["id_empresa"].label_from_instance = lambda obj: obj.nombre
        self.fields["id_estado"].label_from_instance = lambda obj: obj.nombre
        self.fields["usuario_alta"].label_from_instance = lambda obj: obj.username

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar la etiqueta que se muestra para cada empresa
        self.fields["id_empresa"].label_from_instance = lambda obj: obj.codigo_documento
    """

    """
    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        self.fields['codigoEstado'].widget.attrs['class'] = 'form-control'
        self.fields['nombreEstado'].widget.attrs['class'] = 'form-control'
        self.fields['fechaRegistro'].widget.attrs['class'] = 'form-control'
    """
