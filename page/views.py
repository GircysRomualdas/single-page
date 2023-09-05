from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    context = {}
    return render(request, 'base.html', context)

def routeView(request, page):
    context = {
        'temp': 'temp text test',
    }
    print(page)
    return render(request, page + '.html', context)
