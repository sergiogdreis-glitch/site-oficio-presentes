from django.db import models

# 1. Criamos a Categoria primeiro
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Nome sem espaços para usar na URL (ex: dia-das-maes)")

    def __str__(self):
        return self.nome

# 2. Atualizamos a Cesta para pertencer a uma Categoria
class Cesta(models.Model):
    # A linha abaixo é a ponte mágica (ForeignKey)
    categoria = models.ForeignKey(Categoria, related_name='cestas', on_delete=models.CASCADE, null=True)
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='cestas/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    # 3. Tabela para as fotos extras (Galeria)
class ImagemCesta(models.Model):
    # A ponte que liga várias fotos a uma única Cesta
    cesta = models.ForeignKey(Cesta, related_name='imagens_galeria', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='cestas/galeria/')

    def __str__(self):
        return f"Foto extra de: {self.cesta.nome}"