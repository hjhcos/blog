"""hjhcos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.shortcuts import render


def home(request, *args, **kwargs):

    blogs_head = '目录'

    blogs = [
        {
            'url': '/',
            'title': '文章标题1',
            'read': 13,
        },
        {
            'url': '/',
            'title': '文章标题2',
            'read': 12,
        },
        {
            'url': '/',
            'title': '文章标题3',
            'read': 132,
        },
        {
            'url': '/',
            'title': '文章标题4',
            'read': 136,
        },
    ]

    apis_head = '目录'
    apis = [
        {
            'url': '/',
            'title': 'api1',
            'read': 13,
        },
        {
            'url': '/',
            'title': 'api2',
            'read': 12,
        },
        {
            'url': '/',
            'title': 'api3',
            'read': 132,
        },
        {
            'url': '/',
            'title': 'api4',
            'read': 136,
        },
    ]
    return render(request, 'home.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api'))
]
