# Generated by Django 4.1.7 on 2023-03-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_auditor_schema_auditing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schemacertificativo',
            name='auditor_schema',
        ),
        migrations.AddField(
            model_name='auditor',
            name='schema_certificativo',
            field=models.ManyToManyField(to='app.schemacertificativo'),
        ),
    ]
