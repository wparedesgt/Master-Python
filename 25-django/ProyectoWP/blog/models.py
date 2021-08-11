from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description= models.CharField(max_length=255, verbose_name='Descripcion')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name= 'Contenido')
    image = models.ImageField(default= 'null', verbose_name='Imagen', upload_to = "articles")
    public= models.BooleanField(verbose_name='Publicado?')
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name='Categorias', blank=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at= models.DateTimeField(auto_now=True, verbose_name='Modificado el')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


