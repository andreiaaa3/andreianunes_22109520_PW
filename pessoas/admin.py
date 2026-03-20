from django.contrib import admin
from models import Pessoa

class Pessoa (admin.ModelAdmin):
    list_display = ("nome", "idade")
    ordering = ("nome", "idade")
    search_fields = ("nome", "idade")

admin.site.register(Pessoa)