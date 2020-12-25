from django.shortcuts import render

# Create your views here.


def blog(request, *args, **kwargs):
    html = 'blog'
    return render(request, 'blog.html', locals())


def write(request):
    html = 'write'
    return render(request, 'blog/write.html', locals())

