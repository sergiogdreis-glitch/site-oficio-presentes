from django.contrib import admin
from .models import Categoria, Cesta, ImagemCesta

# Isso cria aquele bloco extra de fotos dentro da página da cesta
class ImagemCestaInline(admin.TabularInline):
    model = ImagemCesta
    extra = 1  # Deixa sempre 1 espaço em branco pronto para uma nova foto

class CestaAdmin(admin.ModelAdmin):
    inlines = [ImagemCestaInline]
    list_display = ['nome', 'preco', 'categoria', 'disponivel']

admin.site.register(Categoria)
admin.site.register(Cesta, CestaAdmin)