# Generated by Django 4.1.7 on 2023-03-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auditor_disponibile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagraficasiticliente',
            name='anno_audit',
            field=models.CharField(choices=[('ISO 45001:2018', (('1', '022... - ISO 45001'), ('2', '2023'))), ('ISO 14001:2018', (('1', '2022'), ('2', '2023'))), ('ISO 9001:2015', (('1', '2022'), ('2', '2023')))], max_length=30),
        ),
    ]
