# Generated by Django 4.1.7 on 2023-03-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_anagraficasiticliente_anno_audit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagraficasiticliente',
            name='anno_audit',
            field=models.CharField(choices=[('ISO 45001:2018', (('1', '022... - ISO 45001'), ('2', '2023'))), ('ISO 14001:2018', (('1', '2100'), ('2', '2023'))), ('ISO 9001:2015', (('1', '2022'), ('2', '2023')))], max_length=30),
        ),
    ]
