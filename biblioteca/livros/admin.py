from django.contrib import admin

from .models import Livro


class ExibeLivro(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'anopublicacao', 'isbn')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('anopublicacao',)
    list_per_page = 2


# Adicionar o app no settings.py o proprio app, caso contrário o modelo não será adicionado no db
admin.site.register(Livro, ExibeLivro)
