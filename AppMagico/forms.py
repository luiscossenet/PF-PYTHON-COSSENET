from django import forms
from .models import Estado, Empresa, Cargos


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

    id_empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Empresa",
        empty_label="Seleccione una empresa",
    )

    id_estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Estado",
        empty_label="Seleccione un estado",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar la etiqueta que se muestra para cada empresa
        self.fields["id_empresa"].label_from_instance = lambda obj: obj.nombre
        self.fields["id_estado"].label_from_instance = lambda obj: obj.nombre

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
