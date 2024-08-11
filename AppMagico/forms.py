from django import forms


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
    """
    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        self.fields['codigoEstado'].widget.attrs['class'] = 'form-control'
        self.fields['nombreEstado'].widget.attrs['class'] = 'form-control'
        self.fields['fechaRegistro'].widget.attrs['class'] = 'form-control'
    """
