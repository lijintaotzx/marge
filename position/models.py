# coding=utf-8
from django.db import models

# Create your models here.
from user.models import UserProfile


class Position(models.Model):
    userprofile = models.ForeignKey(UserProfile, related_name='position')
    country = models.CharField('国家', max_length=24)
    province = models.CharField('省份', max_length=24)
    city = models.CharField('市', max_length=24)

    def __str__(self):
        return '{}-{}-{}'.format(self.country, self.province, self.city)

    class Meta:
        verbose_name = '位置信息'
        verbose_name_plural = '位置信息'
