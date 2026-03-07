from django.contrib import admin
from .models import Cesta, Categoria

# Registrando a Categoria para aparecer no painel
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)} # Preenche o slug automaticamente

# Registrando a Cesta
@admin.register(Cesta)
class CestaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'disponivel')
    list_filter = ('categoria', 'disponivel')