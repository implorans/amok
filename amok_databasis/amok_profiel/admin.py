from django.contrib import admin
from .models import adres, profiel, voertuig
from django.utils.html import mark_safe


class ProfielAdmin(admin.ModelAdmin):
    list_display = ('idnommer', 'van', 'vollename', 'noemnaam','epos', 'get_foto')
    
    def get_foto(self, obj):
        if obj.foto:
            return mark_safe(f'<img src="{obj.foto.url}" width="75" />')
        else:
            return "-"
    get_foto.short_description = "Profiel Foto"
    

class AdresAdmin(admin.ModelAdmin):
    list_display = ('adres', 'dorp', 'provinsie', 'poskode')
    
class VoertuigAdmin(admin.ModelAdmin):
    list_display = ('registrasie','fabrikaat', 'kleur')
    
# Register your models here.
admin.site.register(adres, AdresAdmin)
admin.site.register(profiel, ProfielAdmin)
admin.site.register(voertuig, VoertuigAdmin)

admin.site.site_header = "Amok Databasis Administrasie"
admin.site.site_title = "Amok Databasis"
admin.site.index_title = "Amok Databasis"
