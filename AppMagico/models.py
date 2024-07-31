from django.db import models

'''
crear modelo con clases y relaciones:
Estado (id, nombre, fecha_alta)
Empresa (id, nombre, id_estado, usuario_alta,fecha alta)
Cargos(id, nombre, id_empresa, id_estado, usuario_alta,fecha alta)
Tipo_Documento(id, codigo_documento, nombre, id_estado, usuario_alta, fecha alta)
Usuarios(id, codigo_documento, nombre, apellido, id_empresa, id_cargo, id_estado, prefijo ,telefono ,direccion,ciudad,estado,pais,correo_electronico,usuario_alta,fecha_alta)

'''
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    id_estado = models.CharField(max_length=2, unique=True,null=True)
    nombre = models.CharField(max_length=255,null=True)
    fecha_alta = models.DateField()
    def __str__(self):
        return f"Codigo:{self.id}, Codigo_Estado: {self.id_estado},Nombre_Estado: {self.nombre}, Fecha_Alta: {self.fecha_alta}"

class Tipo_Documento(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_documento = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario_alta = models.CharField(max_length=255)
    fecha_alta = models.DateField()
    def __str__(self):
        return f"ID Tipo Documento: {self.id}, Codigo Tipo Documento: {self.codigo_documento}, Nombre Tipo Documento: {self.nombre}, Codigo Estado: {self.id_estado}, Usuario Alta: {self.usuario_alta}, Fecha de Alta: {self.fecha_alta}"


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_documento = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, null=True)
    numero_documento = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario_alta = models.CharField(max_length=255)
    fecha_alta = models.DateField()
    def __str__(self):
        return f"Codigo Empresa: {self.id}, Codigo Documento: {self.codigo_documento}, Numero Documento: {self.numero_documento}, Nombre Empresa: {self.nombre}, Codigo Estado: {self.id_estado}, Usuario Alta: {self.usuario_alta}, Fecha de Alta: {self.fecha_alta}"

class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario_alta = models.CharField(max_length=255)
    fecha_alta = models.DateField()
    def __str__(self):
        return f"Codigo Cargo: {self.id}, Nombre Cargo: {self.nombre}, Codigo Empresa: {self.id_empresa}, Codigo Estado: {self.id_estado}, Usuario Alta: {self.usuario_alta}, Fecha de Alta: {self.fecha_alta}"

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_documento = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    prefijo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    usuario_alta = models.CharField(max_length=255)
    fecha_alta = models.DateField()
    def __str__(self):
        return f"ID Usuario: {self.id}, Codigo Documento: {self.codigo_documento}, Nombre: {self.nombre}, Apellido: {self.apellido}, Codigo Empresa: {self.id_empresa}, Codigo Cargo: {self.id_cargo}, Codigo Estado: {self.id_estado}, Prefijo: {self.prefijo}, Telefono: {self.telefono}, Direccion: {self.direccion}, Ciudad: {self.ciudad}, Estado: {self.estado}, Pais: {self.pais}, Correo Electronico: {self.correo_electronico}, Usuario Alta: {self.usuario_alta}, Fecha de Alta: {self.fecha_alta}"   
    