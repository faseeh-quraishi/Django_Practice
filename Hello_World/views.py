from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"hello/index.html")#HttpResponse('Hello World! This is default Http Response')

def greeting(request, name):
    # if name == 'Faseeh':
        return render(request, "hello/greeting.html",{
            'name': name
            }) 
    #HttpResponse(f'Hi!, this is me, {name}.')
    # else:
    #     return HttpResponse(f'Hello! I am {name}.')