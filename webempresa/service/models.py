from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='service')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    def __str__(self):
        return self.title
