from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.VitrineView.as_view(), name='vitrine'),
    path('cesta/<int:pk>/', views.CestaDetailView.as_view(), name='detalhe_cesta'),
    path('informacoes/', TemplateView.as_view(template_name='loja/informacoes.html'), name='informacoes'),
    path('sobre/', TemplateView.as_view(template_name='loja/sobre.html'), name='sobre'),
    path('contato/', TemplateView.as_view(template_name='loja/contato.html'), name='contato'),
]