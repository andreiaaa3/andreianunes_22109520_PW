from django.contrib import admin

# Register your models here.

from .models import Ginasio

class GinasioAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Ginasio, GinasioAdmin)