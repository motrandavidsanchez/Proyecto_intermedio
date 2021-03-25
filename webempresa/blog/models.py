from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicacion', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categorys = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_post')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    def __str__(self):
        return self.title
