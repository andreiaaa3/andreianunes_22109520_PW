from django.contrib import admin

# Register your models here.

from .models import Receita, Ingrediente

class ReceitaAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome", )
    search_fields = ("nome",)

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Ingrediente)