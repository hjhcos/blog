# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 9:37
# @Author  : hjhcos
# @Email   : hjhcos@hotmail.com
# @File    : urls.py.py
# --------------------------------
from django.conf.urls import url
from blog import views


urlpatterns = [
    url('^$', views.blog, name='blog'),
    url('^write/', views.write),
    url('^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<title>.*?)$', views.display),
]
