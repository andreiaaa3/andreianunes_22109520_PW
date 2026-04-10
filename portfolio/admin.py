from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, CategoriaTecnologia, Tecnologia, Projeto, TFC, Competencia, Formacao, MakingOf


class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "ano", "semestre")
    search_fields = ("nome", "codigo")
    list_filter = ("ano", "semestre")


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "nivel_preferencia")
    search_fields = ("nome",)
    list_filter = ("categoria",)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "unidade_curricular", "data")
    search_fields = ("titulo",)
    list_filter = ("unidade_curricular",)


class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano")
    search_fields = ("titulo", "autor")
    list_filter = ("ano",)


class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data", "entidade_alvo", "usei_ai")
    search_fields = ("titulo", "entidade_alvo")
    list_filter = ("entidade_alvo", "usei_ai")


admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(CategoriaTecnologia)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(Competencia)
admin.site.register(Formacao)
admin.site.register(MakingOf, MakingOfAdmin)