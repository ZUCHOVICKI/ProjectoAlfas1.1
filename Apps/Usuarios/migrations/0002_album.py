# Generated by Django 3.0.3 on 2020-03-24 02:32

import Apps.Usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(upload_to=Apps.Usuarios.models.image_Path)),
            ],
        ),
    ]
