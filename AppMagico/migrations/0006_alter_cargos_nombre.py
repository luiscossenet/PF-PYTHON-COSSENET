# Generated by Django 5.0.7 on 2024-08-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMagico', '0005_alter_empresa_numero_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargos',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
