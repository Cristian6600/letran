# Generated by Django 3.2.12 on 2022-04-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0016_alter_respuesta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='respuesta',
            field=models.TextField(max_length=7500),
        ),
    ]
