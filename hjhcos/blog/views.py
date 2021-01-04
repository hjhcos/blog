from django.shortcuts import render, HttpResponse
from blog import process
from urllib import request
import markdown

# Create your views here.


def blog(requests, *args, **kwargs):
    html = 'blog'
    return render(requests, 'blog.html', locals())


def write(requests):
    # TODO:写文章
    html = 'write'
    return render(requests, 'blog/write.html', locals())


def display(requests, year, month, day, title):
    # TODO:文章内容加载
    # blog / 2020 / 12 / 27 / blog
    url = f'blog/{year}/{month}/{day}/{title}'
    file = process.blog.get_file(url.encode('utf8'))
    print(file)
    html = request.urlopen(file).read().decode('utf-8')
    html = markdown.markdown(html)
    return HttpResponse(html)

