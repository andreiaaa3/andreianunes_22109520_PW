from django.contrib import admin

# Register your models here.

from .models import Festival


class FestivalAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ( "nome",)
    search_fields = ("nome",)

admin.site.register(Festival, FestivalAdmin)