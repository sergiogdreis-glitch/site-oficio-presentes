from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # O segredo é o 'urls' no plural!
    path('admin/', admin.site.urls), 
    
    # Isso manda o Django olhar o arquivo da pasta 'loja'
    path('', include('loja.urls')), 
]

# Configuração para as imagens das cestas aparecerem
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)