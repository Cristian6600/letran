# Generated by Django 3.2.12 on 2022-04-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0017_alter_respuesta_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='tipo',
            field=models.CharField(choices=[('Abierto', 'Abierto'), ('Pendiente', 'Pendiente'), ('Cerrado', 'Cerrado')], default='Abierto', max_length=9),
        ),
    ]