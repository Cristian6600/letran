# Generated by Django 3.2.12 on 2022-03-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0006_pqr_aceptar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pqr',
            name='otro_cual',
        ),
        migrations.AddField(
            model_name='pqr',
            name='tipo_soli',
            field=models.CharField(choices=[('PE', 'Petición'), ('QUEJA', 'Queja'), ('INDEM', 'Indemnización'), ('SUG', 'Sugerencia')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
