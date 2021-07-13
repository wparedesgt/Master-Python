from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to = "articles")
    public = models.BooleanField(verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="Modificado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-id']

    def __str__(self) -> str:
        if self.public:
            publico = 'Publicado'
        else:
            publico = 'Privado'

        return f"{self.title}  ({publico})"




class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"





