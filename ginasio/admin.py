from django.contrib import admin

# Register your models here.

from .models import Ginasio, Membro,Sessao, PersonalTrainer

class GinasioAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Ginasio, GinasioAdmin)
admin.site.register(PersonalTrainer)
admin.site.register(Membro)
admin.site.register(Sessao)