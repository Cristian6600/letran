# Generated by Django 3.2.12 on 2022-04-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0013_alter_respuesta_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
