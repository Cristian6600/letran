# Generated by Django 3.2.12 on 2022-03-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0005_alter_pqr_tipo_do'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqr',
            name='aceptar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
