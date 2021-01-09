from django.shortcuts import render

# Create your views here.


def api(request, *args, **kwargs):
    title = 'api'
    return render(request, 'api.html', locals())
