from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'

    title = models.CharField(verbose_name="Titulo", max_length=100)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    def __str__(self):
        return self.title
