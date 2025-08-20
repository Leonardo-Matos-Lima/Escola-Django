from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

"""
As classe admin servem para instanciar como os dados aparecerão na tela do link de admin
serching_fields = Variavel que diz quais dados podem ser usados para pesquisar um estudante ou curso.
ordering = Variavel que diz por qual dado os resultados serão ordenados.
"""
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)
    ordering = ('nome',)

admin.site.register(Estudante,Estudantes)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)