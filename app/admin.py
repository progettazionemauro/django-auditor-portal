# app/admin.py
from django.contrib import admin
from django import forms
from .models import *

from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PhoneForm(forms.ModelForm):   # classe per registrare il widget per l'inserimento del numero di telefono
    class Meta:
        widgets = {
            'cellulare_auditor':PhoneNumberPrefixWidget(initial='IT'),
            'cellulare_ref_cliente':PhoneNumberPrefixWidget(initial='IT'),
        }
        
@admin.register(Auditor)                # registrazione in admin del widget per l'inseimento del n° telefonico
class AuditorAdmin(admin.ModelAdmin):
    form = PhoneForm

@admin.register(SchemaCertificativo)
class SchemaCertificativoAdmin(admin.ModelAdmin):
    pass


""" @admin.register(AnagraficaTeamCliente)
class AnagraficaTeamClienteAdmin(admin.ModelAdmin):
    form=PhoneForm
    pass """





