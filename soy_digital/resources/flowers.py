from django.db import models
from django.contrib import admin

from BotMessenger import settings


class FlowersModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de flor')
    description = models.CharField(max_length=200, verbose_name='Descripcion')
    image = models.ImageField(null=True, verbose_name='Fotografia')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Fecha de publicacion')

    def get_image(self):
        return "%s%s" % (settings.MEDIA_ABSOLUTE_DOMAIN, self.image.url)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Flor"
        verbose_name_plural = "Flores"


class FlowerAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image')
    list_display = ('name', 'description', 'pub_date',)
    list_filter = ('pub_date',)
    search_fields = ('name',)


admin.site.register(FlowersModel, FlowerAdmin)
