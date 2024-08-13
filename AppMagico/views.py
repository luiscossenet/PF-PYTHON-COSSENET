from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.template import Template, Context, loader
from AppMagico.forms import *
from django.shortcuts import get_object_or_404
import requests

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


#####################TipoDocumento
# CRUD operations for each model
def CrearTipoDocumento(request):
    if request.method == "POST":
        codigoDocumento = request.POST["codigo_documento"]
        nombreEstado = request.POST["nombre"]
        idEstado = request.POST["id_estado"]
        usuarioAlta = request.POST["usuario_alta"]
        fechaAlta = request.POST["fecha_alta"]
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


############CrearCargos


# CRUD operations for each model
def CrearCargos(request):
    if request.method == "POST":
        idEstado = request.POST["codigoEstado"]
        nombreEstado = request.POST["nombreEstado"]
        fechaAlta = request.POST["fechaRegistro"]
        estado = Estado(id_estado=idEstado, nombre=nombreEstado, fecha_alta=fechaAlta)
        try:
            estado.save()
            mensaje = f"Estado: {nombreEstado} con codigo: {idEstado} y fecha de registro: {fechaAlta}"
            statuscode = 200
            print("Estado grabado")
        except:
            mensaje = "El registro ya existe"
            statuscode = 200
            print("El registro ya existe")
        print({"mensaje": mensaje, "status_code": statuscode})
        # mensaje = "Estado grabado exitosamente"
        return render(request, "pages/addEstados.html", {"mensaje": mensaje})

    return render(request, "pages/addEstados.html")


# CRUD operations for each model
def SelectCargos(request):
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


def cursoFormulario(request):
    print(request.method + "Hola")
    if request.method == "POST":
        print("Hola Post")
        # curso =  Curso(request.post['curso'],(request.post['camada']))

        # curso.save()
        print(request.method)

        return render(request, "index.html")
    # CursoFormulario
    # return render(request,"pages/selEstados.html/")
    return render(request, "pages/cursoFormulario.html")
