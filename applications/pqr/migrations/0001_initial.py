# Generated by Django 3.0.6 on 2022-02-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('otro_cual', models.CharField(max_length=30)),
                ('tipo_do', models.CharField(choices=[('C', 'CC'), ('CE', 'CE')], max_length=4)),
                ('n_documento', models.CharField(max_length=12)),
                ('apellidos', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('n_contacto', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=120)),
                ('n_guia', models.IntegerField()),
                ('desc_pqr', models.TextField()),
            ],
        ),
    ]
