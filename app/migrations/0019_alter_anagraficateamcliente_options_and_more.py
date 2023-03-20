# Generated by Django 4.1.7 on 2023-03-10 07:55

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_anagraficateamcliente_anagraficasiticliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anagraficateamcliente',
            options={'verbose_name': 'Team Cliente', 'verbose_name_plural': 'Team Cliente'},
        ),
        migrations.AddField(
            model_name='anagraficasiticliente',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=1, srid=4326),
            preserve_default=False,
        ),
    ]
