from django.db import models

opciones_alerta = [
    [0, "Aviso"],
    [1, "Incidente"],
    [2, "Sugerencia"],
    [3, "Urgente"],
]

class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    n_bus = models.IntegerField()
    tipo_alarma = models.IntegerField(choices=opciones_alerta)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.descripcion

#################################################################################

opciones_solicitud = [
    [0, "Permiso Dia Completo"],
    [1, "Tarde Libre"],
    [2, "Mañana libre"],
    [3, "1/2 Libre"],
]

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_permiso = models.DateField()
    motivo = models.IntegerField(choices=opciones_solicitud)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre

############################################################################

opciones_check = [
    [0, "Si"],
    [1, "No"]
]

class Checklist(models.Model):
    id_check = models.AutoField(primary_key=True)
    kilometraje = models.IntegerField()
    fecha_registro = models.DateField()
    neumaticos = models.IntegerField(choices=opciones_check)
    correas = models.IntegerField(choices=opciones_check)
    aceite = models.IntegerField(choices=opciones_check)
    mangueras = models.IntegerField(choices=opciones_check)
    direccion = models.IntegerField(choices=opciones_check)
    liquido_frenos = models.IntegerField(choices=opciones_check)
    pastillas = models.IntegerField(choices=opciones_check)
    balatas = models.IntegerField(choices=opciones_check)
    observaciones = models.CharField(max_length=300)

    def __str__(self):
            return self.observaciones

####################################################################################
            
class Ot_mecanicos(models.Model):
    id_ot = models.IntegerField(primary_key=True)
    fecha_ot = models.DateField()
    n_bus = models.IntegerField()
    id_check = models.ForeignKey('Checklist', on_delete=models.PROTECT, db_column='id_check')
    trabajo_realizado = models.CharField(max_length=500)
    def __str__(self):
            return self.trabajo_realizado
