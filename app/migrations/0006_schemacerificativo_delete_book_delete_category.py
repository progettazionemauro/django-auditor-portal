# Generated by Django 4.1.7 on 2023-02-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_profile_auditor_nome_auditor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemaCerificativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_certificazione', models.CharField(choices=[('1', 'ISO 9001:2015'), ('2', 'ISO 14001:2018'), ('3', 'ISO 45001:2015')], default='ISO 9001:2015', max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
