from django.views.generic import ListView, DetailView
from .models import Cesta, Categoria

class VitrineView(ListView):
    model = Cesta
    template_name = 'loja/vitrine.html'
    context_object_name = 'cestas'

    # 1. Envia a lista de categorias para a tela criar os botões
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    # 2. Faz o filtro funcionar quando clica no botão
    def get_queryset(self):
        queryset = Cesta.objects.filter(disponivel=True) # Mostra só as disponíveis
        categoria_id = self.request.GET.get('categoria')
        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
            
        return queryset

class CestaDetailView(DetailView):
    model = Cesta
    template_name = 'loja/cesta_detail.html'
    context_object_name = 'cesta'