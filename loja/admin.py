from django.contrib import admin

# Register your models here.

from .models import Loja,Categoria,Cliente,Morada,Pedido,Produto

class LojaAdmin (admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ( "nome",)
    search_fields = ("nome",)

admin.site.register(Loja, LojaAdmin)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Morada)
admin.site.register(Pedido)
admin.site.register(Produto)