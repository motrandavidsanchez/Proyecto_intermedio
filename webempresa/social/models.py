from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'

    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=100)
    url = models.URLField(verbose_name="Enlace", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    def __str__(self):
        return self.name
