from django.contrib import admin
from .models import *


# Listar en el display de la tabla de la base de datos los campos que se desean mostrar
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("id_estado", "nombre", "fecha_alta")
    search_fields = ("id_estado", "nombre")
    list_filter = ("id_estado", "nombre")
    ordering = ("id_estado", "nombre")
    list_per_page = 10


class CargosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "id_empresa", "id_estado", "usuario_alta", "fecha_alta")
    search_fields = ("nombre", "id_empresa", "id_estado", "usuario_alta", "fecha_alta")
    list_filter = ("nombre", "id_empresa", "id_estado", "usuario_alta", "fecha_alta")
    ordering = ("nombre", "id_empresa", "id_estado", "usuario_alta", "fecha_alta")
    list_per_page = 10


class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_documento",
        "numero_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    search_fields = (
        "codigo_documento",
        "numero_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    list_filter = (
        "codigo_documento",
        "numero_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    ordering = (
        "codigo_documento",
        "numero_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    list_per_page = 10


class Tipo_DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    search_fields = (
        "codigo_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    list_filter = (
        "codigo_documento",
        "nombre",
        "id_estado",
        "usuario_alta",
        "fecha_alta",
    )
    ordering = ("codigo_documento", "nombre", "id_estado", "usuario_alta", "fecha_alta")
    list_per_page = 10


class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_documento",
        "nombre",
        "apellido",
        "id_empresa",
        "id_cargo",
    )
    search_fields = (
        "codigo_documento",
        "nombre",
        "apellido",
        "id_empresa",
        "id_cargo",
    )
    list_filter = (
        "codigo_documento",
        "nombre",
        "apellido",
        "id_empresa",
        "id_cargo",
    )
    ordering = ("codigo_documento", "nombre", "apellido", "id_empresa", "id_cargo")
    list_per_page = 10


# Register your models here.
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Tipo_Documento, Tipo_DocumentoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Cargos, CargosAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
