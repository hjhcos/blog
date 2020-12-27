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

from blog import process


def page_not_found(request):
    html = '404'
    return render(request, '404.html')


def feedback(request, **kwargs):
    html = '反馈'
    return render(request, 'feedback.html')


def home(request, *args, **kwargs):
    html = '首页'
    blogs = process.blog.get_all()
    print(blogs)
    return render(request, 'base/base.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^feedback/*?', feedback),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api')),
]

handler404 = page_not_found
