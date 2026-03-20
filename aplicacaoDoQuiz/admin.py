from django.contrib import admin

# Register your models here.

from .models import Festival, Banda, Genero


class FestivalAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ( "nome",)
    search_fields = ("nome",)

admin.site.register(Festival, FestivalAdmin)
admin.site.register(Banda)
admin.site.register(Genero)

