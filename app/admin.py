# app/admin.py
from django.contrib import admin
from django.utils.html import format_html
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
    
@admin.register(NazioniEntiFinanziari)
class NazioniEntiFinanziariAdmin(admin.ModelAdmin):
    list_display=["nazione", "nome_ente_finanziario", "url_ente_finanziario", "Link"]
    def Link(self, obj):
       # return format_html('<a  href="https://127.0.0.1:8000/product/{0}" >{1}</a>',obj.id, obj.email_auditor) #url con parametri
        return format_html(' <a href={0} target=”_blank”>{1}</a>',obj.url_ente_finanziario, obj.nazione)
    

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
    list_display=["nome_auditor", "email_auditor", "cellulare_auditor", "Link_schema_certificativo"]
    form = PhoneForm
    
    def Link_schema_certificativo(self, obj):
       # return format_html('<a  href="https://127.0.0.1:8000/product/{0}" >{1}</a>',obj.id, obj.email_auditor) #url con parametri
        return format_html('<a  href="https://en.wikipedia.org/wiki/Nigeria" >{1}</a>',obj.id, obj.email_auditor)

    
    
      

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





