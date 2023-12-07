from django.contrib import admin
from appLacrei.models import Profissional, Consulta

class Profissionais(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nome_social', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome_social', 'cpf', 'nome')
    list_per_page = 30

admin.site.register(Profissional, Profissionais)

class Consultas(admin.ModelAdmin):
    list_display = ('id', 'data', 'profissional')
    list_display_links = ('id', 'data', 'profissional')
    search_fields = ('id', 'data', 'profissional')
    list_per_page = 30

admin.site.register(Consulta, Consultas)

