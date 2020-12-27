from django.shortcuts import render, HttpResponse
from blog import process

# Create your views here.


def blog(request, *args, **kwargs):
    html = 'blog'
    return render(request, 'blog.html', locals())


def write(request):
    # TODO:写文章
    html = 'write'
    return render(request, 'blog/write.html', locals())


def display(request, year, month, day, title):
    # TODO:文章内容加载
    return HttpResponse(process.blog.show_tags())

