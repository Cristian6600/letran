# Generated by Django 3.2.12 on 2022-06-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0019_contacto_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='observacion',
            field=models.TextField(max_length=150),
        ),
    ]
