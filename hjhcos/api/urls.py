# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 23:39
# @Author  : hjhcos
# @Email   : hjhcos@hotmail.com
# @File    : urls.py.py
# --------------------------------

from django.conf.urls import url
from api import views


urlpatterns = [
    url('^$', views.api, name='api'),

]
