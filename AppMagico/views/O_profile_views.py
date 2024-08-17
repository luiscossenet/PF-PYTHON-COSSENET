from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import *
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


# CRUD operations for each model


#####################ESTADO ADD ############################


def estadosViewAdd(request):
    if request.method == "POST":

        myFormEstado = EstadoForm(request.POST)  # Aqui me llega la informacion del html
        print(myFormEstado)

        if myFormEstado.is_valid():

            informacion = myFormEstado.cleaned_data
            estado = Estado(
                id_estado=informacion["codigoEstado"],
                nombre=informacion["nombreEstado"],
                fecha_alta=informacion["fechaRegistro"],
            )
            try:
                estado.save()
                mensaje = f"Registro Creado. Estado: {estado.nombre} con codigo: {estado.id_estado} y fecha de registro: {estado.fecha_alta}"
                statuscode = 200
                swEstado = True
                # print("Estado grabado")
            except:
                mensaje = f"Ya existe registro. Estado: {estado.nombre} con codigo: {estado.id_estado}"
                statuscode = 200
                swEstado = False
                # print("El registro ya existe")
            # print({"mensaje": mensaje, "status_code": statuscode})
            # mensaje = "Estado grabado exitosamente"
            myFormEstado = EstadoForm()
            return render(
                request,
                "pages/estadosAdd.html",
                {"pFormEstado": myFormEstado, "mensaje": mensaje},
            )
    else:
        myFormEstado = EstadoForm()

    return render(request, "pages/estadosAdd.html", {"pFormEstado": myFormEstado})


#####################ESTADO SELECT ############################
def estadosViewSelect(request):
    if request.method == "POST":

        myFormEstado = EstadoSelectForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(myFormEstado)

        if myFormEstado.is_valid():

            informacion = myFormEstado.cleaned_data
            estado = Estado(nombre=informacion["nombreEstado"])
            myFormEstado = EstadoSelectForm()
            try:
                resultadoConsulta = Estado.objects.filter(
                    nombre__icontains=estado.nombre
                )
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado",
                    "pFormEstado": myFormEstado,
                }

                # print("Estado grabado")
            except:
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado, sin regsitros",
                    "pFormEstado": myFormEstado,
                }
                # print("El registro ya existe")
            # print({"mensaje": mensaje, "status_code": statuscode})
            # mensaje = "Estado grabado exitosamente"
            # myFormEstado = EstadoForm()
            return render(request, "pages/estadosSelect.html", context)
    else:
        myFormEstado = EstadoSelectForm()

    return render(request, "pages/estadosSelect.html", {"pFormEstado": myFormEstado})


#####################LISTAR ESTADO SELECT ############################
def estadosViewSelectAll(request):
    if request.method == "POST":

        myFormEstado = EstadoSelectAllForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(myFormEstado)

        if myFormEstado.is_valid():

            informacion = myFormEstado.cleaned_data
            estado = Estado(nombre=informacion["nombreEstado"])
            myFormEstado = EstadoSelectAllForm()
            try:
                resultadoConsulta = Estado.objects.filter(
                    nombre__icontains=estado.nombre
                )
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado",
                    "pFormEstado": myFormEstado,
                }

                # print("Estado grabado")
            except:
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado, sin regsitros",
                    "pFormEstado": myFormEstado,
                }
                # print("El registro ya existe")
            # print({"mensaje": mensaje, "status_code": statuscode})
            # mensaje = "Estado grabado exitosamente"
            # myFormEstado = EstadoForm()
            return render(request, "pages/estadosSelectAll.html", context)
    else:
        myFormEstado = EstadoSelectAllForm()

    return render(request, "pages/estadosSelectAll.html", {"pFormEstado": myFormEstado})


##################### UPDATE ESTADO SELECT ############################
def estadosViewUpdate(request):
    if request.method == "POST":

        myFormEstado = EstadoSelectAllForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(myFormEstado)

        if myFormEstado.is_valid():

            informacion = myFormEstado.cleaned_data
            estado = Estado(nombre=informacion["nombreEstado"])
            myFormEstado = EstadoSelectAllForm()
            try:
                resultadoConsulta = Estado.objects.filter(
                    nombre__icontains=estado.nombre
                )
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado",
                    "pFormEstado": myFormEstado,
                }
            except:
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado, sin regsitros",
                    "pFormEstado": myFormEstado,
                }
            return render(request, "pages/estadosUpdate.html", context)
    else:
        myFormEstado = EstadoSelectAllForm()

    return render(request, "pages/estadosUpdate.html", {"pFormEstado": myFormEstado})


##################### UPDATE ESTADO ROW ############################
def estadosViewUpdateRow(request, id):
    # estado = get_object_or_404(Estado, id=id)
    estado = Estado.objects.get(id=id)
    data = {
        "Nombre": "Hola",
        "id": estado.id,
        "codigoEstado": estado.id_estado,
        "nombreEstado": estado.nombre,
        "fechaRegistro": estado.fecha_alta.strftime("%Y-%m-%d"),
    }
    if request.method == "POST":
        myFormEstado = EstadoUpdForm(data)  # Ligamos el formulario al objeto existente
        # Aqui me llega la informacion del html
        if myFormEstado.is_valid():
            informacion = myFormEstado.cleaned_data.copy()
            informacion["fechaRegistro"] = informacion["fechaRegistro"].strftime(
                "%Y-%m-%d"
            )
            myFormEstado = EstadoUpdForm(informacion)
            return render(
                request, "pages/estadosUpdateRow.html", {"pFormEstado": myFormEstado}
            )

    else:
        myFormEstado = EstadoSelectAllForm()

    return render(request, "pages/estadosUpdate.html", {"pFormEstado": myFormEstado})


##################### UPDATE ESTADO ROW COMMIT ############################
def estadosViewUpdateRowCommit(request):
    if request.method == "POST":
        myFormEstado = EstadoUpdForm(
            request.POST
        )  # Ligamos el formulario al objeto existente
        if myFormEstado.is_valid():
            informacion = myFormEstado.cleaned_data
            estado = Estado(
                id=informacion["id"],
                id_estado=informacion["codigoEstado"],
                nombre=informacion["nombreEstado"],
                fecha_alta=informacion["fechaRegistro"],
            )
            try:
                estado.save()
                mensaje = f"Registro Actualizado. Estado: {estado.nombre} con codigo: {estado.id_estado} y fecha de registro: {estado.fecha_alta}"
                statuscode = 200
                swEstado = True
                myFormEstado = EstadoSelectAllForm()
            except:
                mensaje = f"Error al actualizar. Estado: {estado.nombre} con codigo: {estado.id_estado}"
                statuscode = 500
                swEstado = False
                myFormEstado = EstadoSelectAllForm()
            return redirect("vEstadosUpdate")
        else:
            myFormEstado = EstadoSelectAllForm()
    return redirect("vEstadosUpdate")


##################### DELETE ESTADO SELECT ############################
def estadosViewDelete(request):
    if request.method == "POST":

        myFormEstado = EstadoSelectAllForm(
            request.POST
        )  # Aqui me llega la informacion del html
        print(myFormEstado)

        if myFormEstado.is_valid():

            informacion = myFormEstado.cleaned_data
            estado = Estado(nombre=informacion["nombreEstado"])
            myFormEstado = EstadoSelectAllForm()
            try:
                resultadoConsulta = Estado.objects.filter(
                    nombre__icontains=estado.nombre
                )
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado",
                    "pFormEstado": myFormEstado,
                }

            except:
                context = {
                    "mensaje": resultadoConsulta,
                    "statuscode": 200,
                    "swEstado": True,
                    "respuesta": "Estado consultado, sin regsitros",
                    "pFormEstado": myFormEstado,
                }
            return render(request, "pages/estadosDelete.html", context)
    else:
        myFormEstado = EstadoSelectAllForm()

    return render(request, "pages/estadosDelete.html", {"pFormEstado": myFormEstado})


##################### DELETE ESTADO ROW ############################
def estadosViewDeleteRow(request, id):
    estado = Estado.objects.get(id=id)
    data = {
        "Nombre": "Hola",
        "id": estado.id,
        "codigoEstado": estado.id_estado,
        "nombreEstado": estado.nombre,
        "fechaRegistro": estado.fecha_alta.strftime("%Y-%m-%d"),
    }
    if request.method == "POST":
        myFormEstado = EstadoUpdForm(data)  # Ligamos el formulario al objeto existente
        # Aqui me llega la informacion del html
        if myFormEstado.is_valid():
            informacion = myFormEstado.cleaned_data.copy()
            informacion["fechaRegistro"] = informacion["fechaRegistro"].strftime(
                "%Y-%m-%d"
            )
            myFormEstado = EstadoDelForm(informacion)
            return render(
                request, "pages/estadosDeleteRow.html", {"pFormEstado": myFormEstado}
            )

    else:
        myFormEstado = EstadoSelectAllForm()

    return render(request, "pages/estadosDelete.html", {"pFormEstado": myFormEstado})


##################### DELETE ESTADO ROW COMMIT ############################
def estadosViewDeleteRowCommit(request):
    if request.method == "POST":
        myFormEstado = EstadoUpdForm(
            request.POST
        )  # Ligamos el formulario al objeto existente
        if myFormEstado.is_valid():
            informacion = myFormEstado.cleaned_data
            estado = Estado(
                id=informacion["id"],
                id_estado=informacion["codigoEstado"],
                nombre=informacion["nombreEstado"],
                fecha_alta=informacion["fechaRegistro"],
            )
            try:
                estado.delete()
                mensaje = f"Registro Actualizado. Estado: {estado.nombre} con codigo: {estado.id_estado} y fecha de registro: {estado.fecha_alta}"
                statuscode = 200
                swEstado = True
                myFormEstado = EstadoSelectAllForm()
            except:
                mensaje = f"Error al actualizar. Estado: {estado.nombre} con codigo: {estado.id_estado}"
                statuscode = 500
                swEstado = False
                myFormEstado = EstadoSelectAllForm()
            return redirect("vEstadosDelete")
        else:
            myFormEstado = EstadoSelectAllForm()
    return redirect("vEstadosDelete")


#######CLASES BASADAS EN VISTAS ############################


class CargosListView(LoginRequiredMixin, ListView):
    model = Cargos
    context_object_name = "cargos"
    ordering = ["nombre"]
    paginate_by = 10
    mensaje = "Cargos"
    # context = {"mensaje": mensaje}
    template_name = "pages/cargosSelect.html"

    def get_context_data(self, **kwargs):
        # Obtiene el contexto base de la superclase
        context = super().get_context_data(**kwargs)
        # Añade una variable personalizada al contexto
        context["mensaje"] = "Cargos"
        return context


class CargosDetailView(LoginRequiredMixin, DetailView):
    model = Cargos
    template_name = "pages/cargosSelectDetail.html"
    context_object_name = "cargos"


class CargosCreateView(LoginRequiredMixin, CreateView):
    model = Cargos
    form_class = CargosForm
    template_name = "pages/cargosAdd.html"
    success_url = reverse_lazy("vCargosSelect")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Cargos"

        # Add the result of CargosListView to the context
        cargos_list = Cargos.objects.all()
        context["cargos"] = cargos_list

        return context


class CargosUpdateView(LoginRequiredMixin, ListView):
    model = Cargos
    context_object_name = "cargos"
    ordering = ["nombre"]
    paginate_by = 10
    mensaje = "Cargos"
    template_name = "pages/cargosUpdate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Cargos"

        # Add the result of CargosListView to the context
        cargos_list = Cargos.objects.all()
        context["cargos"] = cargos_list

        return context


class CargosUpdateRowView(LoginRequiredMixin, UpdateView):
    model = Cargos
    # form_class = CargosForm
    template_name = "pages/cargosUpdateRow.html"
    success_url = reverse_lazy("vCargosUpdate")
    fields = ["nombre", "id_empresa", "id_estado"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Cargos"

        # Add the result of CargosListView to the context
        cargos_list = Cargos.objects.all()
        context["cargos"] = cargos_list

        return context


class CargosDeleteView(LoginRequiredMixin, ListView):
    model = Cargos
    context_object_name = "cargos"
    ordering = ["nombre"]
    paginate_by = 10
    mensaje = "Cargos"
    template_name = "pages/cargosDelete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Cargos"

        # Add the result of CargosListView to the context
        cargos_list = Cargos.objects.all()
        context["cargos"] = cargos_list

        return context


class CargosDeleteRowView(LoginRequiredMixin, DeleteView):
    model = Cargos
    template_name = "pages/cargosDeleteRow.html"
    success_url = reverse_lazy("vCargosDelete")
    # context_object_name = "cargos"
    fields = ["nombre", "id_empresa", "id_estado"]

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Cargos"
    
        # Add the result of CargosListView to the context
        cargos_list = Cargos.objects.all()
        context["cargos"] = cargos_list

        return context
    """


#####################TipoDocumento
# CRUD operations for each model
def CrearTipoDocumento(request):
    print("452", request.method)
    if request.method == "POST":
        if request.POST["codigo_documento"] == True:
            codigoDocumento = request.POST["codigo_documento"]
            nombreEstado = request.POST["nombre"]
            idEstado = request.POST["id_estado"]
            usuarioAlta = request.POST["usuario_alta"]
            fechaAlta = request.POST["fecha_alta"]
            print("460", request.method)
            # Supongamos que tienes una instancia de Estado existente
            # cuando se tiene una llave foranea se debe hacer una consulta para obtener el objeto
            estado_instance = Estado.objects.get(
                id_estado=idEstado
            )  # Cambia el valor según corresponda
            estado = Tipo_Documento(
                codigo_documento=codigoDocumento,
                nombre=nombreEstado,
                id_estado=estado_instance,
                usuario_alta=usuarioAlta,
                fecha_alta=fechaAlta,
            )
            try:
                estado.save()
                mensaje = f"Estado Grabado: {nombreEstado} con codigo: {codigoDocumento} y fecha de registro: {fechaAlta}"
                statuscode = 200
                # print("Estado grabado")
            except:
                mensaje = "El registro ya existe"
                statuscode = 200
                # print("El registro ya existe")
                # print( {'mensaje': mensaje, 'status_code': statuscode})
                # mensaje = "Estado grabado exitosamente"
            return render(request, "pages/addTipoDocumento.html", {"mensaje": mensaje})
        else:
            mensaje = "Debe ingresar el codigo del documento"
            return render(request, "pages/addTipoDocumento.html", {"mensaje": mensaje})

    return render(request, "pages/addTipoDocumento.html")


# CRUD operations for each model
def SelectTipoDocumento(request):
    if request.method == "POST":
        valorConsultado = request.POST["valorConsulta"]
        resultadoConsulta = Tipo_Documento.objects.filter(
            nombre__icontains=valorConsultado
        )
        context = {
            "mensaje": resultadoConsulta,
            "statuscode": 200,
            "respuesta": "Estado consultado",
        }
        return render(request, "pages/selTipoDocumento.html", context)

    return render(request, "pages/selTipoDocumento.html")


#####################TEST ############################


"""
    if request.method == "POST":
        valorConsultado = request.POST["valorConsulta"]
        resultadoConsulta = Estado.objects.filter(nombre__icontains=valorConsultado)
        context = {
            "mensaje": resultadoConsulta,
            "statuscode": 200,
            "respuesta": "Estado consultado",
        }
        return render(request, "pages/selEstados.html", context)

    return render(request, "pages/selEstados.html")
"""

#####################TEST ############################


def test(request):
    return render(request, "test.html")
