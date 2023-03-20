# app/admin.py
from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from django.forms.widgets import TextInput
from django import forms
from .models import *
from django_google_maps.widgets import GoogleMapsAddressWidget
#from .models import Place

# admin.site.register(Place)


""" class SampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': GoogleMapsAddressWidget
        },
        GeoLocationField: {
            'widget': TextInput(attrs={
                'readonly': 'readonly'
            })
        },
    } """
""" @admin.site.register(SampleModelAdmin)
class SampleModelAdminAdmin(admin.ModelAdmin):
    pass """

@admin.register(SchemaCertificativo)
class SchemaCertificativoAdmin(admin.ModelAdmin):
    pass


from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from mapwidgets.widgets import GooglePointFieldInlineWidget


class PhoneForm(forms.ModelForm):   # classe per registrare il widget per l'inserimento del numero di telefono
    class Meta:
        widgets = {
            'cellulare_auditor':PhoneNumberPrefixWidget(initial='IT'),
            'cellulare_ref_cliente':PhoneNumberPrefixWidget(initial='IT'),
        }

@admin.register(Auditor)                # registrazione in admin del widget per l'inseimento del n° telefonico
class AuditorAdmin(admin.ModelAdmin):
    form = PhoneForm

""" @admin.register(SchemaCertificativo)
class SchemaCertificativoAdmin(admin.ModelAdmin):
    pass
 """

@admin.register(AnagraficaTeamCliente)
class AnagraficaTeamClienteAdmin(admin.ModelAdmin):
    form=PhoneForm
    pass 

@admin.register(AnagraficaSitiCliente)
class AnagraficaSitiClienteAdmin(admin.ModelAdmin):
    list_display=('indirizzo_sito', 'ubicazione')
    pass 





