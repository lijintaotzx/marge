# coding=utf-8
from django.conf.urls import url

from .views import UserRegView

urlpatterns = [
    url(r'^register/$', UserRegView.as_view()),

]
# coding=utf-8
