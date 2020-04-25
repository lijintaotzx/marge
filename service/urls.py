# coding=utf-8
from django.conf.urls import url

from .views import SmsService

urlpatterns = [
    url(r'^send_sms/$', SmsService.as_view()),
    url(r'^vcode_ttl/$', SmsService.as_view()),

]
