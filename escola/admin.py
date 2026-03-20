from django.contrib import admin

from .models import Escola, Turma, Aluno, Professor

class EscolaAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Escola, EscolaAdmin)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Professor)