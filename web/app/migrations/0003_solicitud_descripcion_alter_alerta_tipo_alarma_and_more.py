# Generated by Django 4.1.1 on 2023-01-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alerta_n_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='descripcion',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alerta',
            name='tipo_alarma',
            field=models.IntegerField(choices=[[0, 'Aviso'], [1, 'Incidente'], [2, 'Sugerencia'], [3, 'Urgente']]),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='motivo',
            field=models.IntegerField(choices=[[0, 'Permiso Dia Completo'], [1, 'Tarde Libre'], [2, 'Mañana libre'], [3, '1/2 Libre']]),
        ),
    ]