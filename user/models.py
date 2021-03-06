# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    SEX_CHOICE = (
        (1, 'man'),
        (2, 'woman'),
    )
    user = models.OneToOneField(User, related_name='userprofile')
    pn = models.CharField('手机号', max_length=32, null=True, blank=True)
    birthday = models.DateField('生日', auto_now=True)
    age = models.IntegerField('年龄', default=0)
    sex = models.IntegerField('性别', default=1, choices=SEX_CHOICE)

    def __str__(self):
        return '{}:{}'.format(self.user.username, self.pn)

    class Meta:
        verbose_name = '用户关联表'
        verbose_name_plural = '用户关联表'


def userprofile_init(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('UserID:{}, Profile create successful!'.format(instance.id))


post_save.connect(userprofile_init, User)
