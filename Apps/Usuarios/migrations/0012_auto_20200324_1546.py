# Generated by Django 3.0.3 on 2020-03-24 21:46

import Apps.Usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0011_auto_20200324_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='duracion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=Apps.Usuarios.models.image_Path),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='calificacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]