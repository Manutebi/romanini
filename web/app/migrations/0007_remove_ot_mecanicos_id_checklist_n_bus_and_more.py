# Generated by Django 4.1.1 on 2023-01-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_checklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ot_mecanicos',
            name='id',
        ),
        migrations.AddField(
            model_name='checklist',
            name='n_bus',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot_mecanicos',
            name='fecha_ot',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot_mecanicos',
            name='id_check',
            field=models.ForeignKey(db_column='id_check', default=12, on_delete=django.db.models.deletion.PROTECT, to='app.checklist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot_mecanicos',
            name='n_bus',
            field=models.IntegerField(default=0.0005934718100890207),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot_mecanicos',
            name='trabajo_realizado',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ot_mecanicos',
            name='id_ot',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]