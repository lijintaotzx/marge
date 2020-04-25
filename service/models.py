from django.db import models


# Create your models here.

class YunpianService(models.Model):
    api_key = models.CharField('API-KEY', max_length=128)

    def __str__(self):
        pass

    class Meta:
        verbose_name = '云片短信通道'
        verbose_name_plural = '云片短信通道'
