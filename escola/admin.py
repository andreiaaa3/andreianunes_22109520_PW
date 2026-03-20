from django.contrib import admin

from .models import Escola

class EscolaAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Escola, EscolaAdmin)
