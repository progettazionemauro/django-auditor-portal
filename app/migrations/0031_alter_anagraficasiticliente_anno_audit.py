# Generated by Django 4.1.7 on 2023-03-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_anagraficasiticliente_anno_audit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagraficasiticliente',
            name='anno_audit',
            field=models.CharField(choices=[('ISO_45001', '2022 - ISO 45001:2018'), ('ISO_45001', '2023 - ISO 45001:2018'), ('ISO_14001', '2022 - ISO 14001:2018'), ('ISO_14001', '2023 - ISO 14001:2018')], max_length=30),
        ),
    ]
