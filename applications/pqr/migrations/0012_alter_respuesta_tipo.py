# Generated by Django 3.2.12 on 2022-04-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0011_alter_respuesta_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='tipo',
            field=models.CharField(choices=[('A', 'Abierto'), ('P', 'Pendiente'), ('C', 'Cerrado')], max_length=2),
        ),
    ]
