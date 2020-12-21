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

# 配置静态文件
from django.conf.urls.static import static
from django.conf import settings

from django.shortcuts import render


def page_not_found(request):
    return render(request, '404.html')


def feedback(request, **kwargs):
    # with open('feedback.txt', 'a', encoding='utf8') as fd:
    #     fd.write(fb)
    return render(request, 'feedback.html')


def home(request, *args, **kwargs):

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

    return render(request, 'home.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^feedback/*?', feedback),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
