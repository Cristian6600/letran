# Generated by Django 3.2.12 on 2022-03-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqr', '0003_auto_20220317_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
