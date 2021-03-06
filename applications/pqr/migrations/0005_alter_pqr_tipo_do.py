# Generated by Django 3.2.12 on 2022-03-23 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0004_alter_pqr_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='tipo_do',
            field=models.CharField(choices=[('C', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('NIT', 'Nit'), ('TDI', 'Tarjeta de identidad'), ('PSATE', 'Pasaporte'), ('P_P_P_T', 'Persmiso por proteccion temporal'), ('C_V', 'Cédula Venezolana'), ('P_E_D_P', 'Permsio especial de permanencia')], max_length=8),
        ),
    ]
