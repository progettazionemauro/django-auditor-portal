# Generated by Django 4.1.7 on 2023-03-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_delete_place_anagraficasiticliente_ubicazione'),
    ]

    operations = [
        migrations.CreateModel(
            name='NazioniEntiFinanziari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazione', models.CharField(max_length=100)),
                ('nome_ente_finanziario', models.CharField(max_length=100)),
                ('url_ente_finanziario', models.URLField(max_length=300, null=True)),
            ],
        ),
    ]
