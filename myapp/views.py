from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def index(req: WSGIRequest):
    return render(req, 'myapp/index.html')

def about(req: WSGIRequest):
    info = {
        'FIO': 'Ков Аск Алекс',
        'rost': '168',
        'weight': '53',
        'age': '16'
    }
    return render(req, 'myapp/about.html', context=info)

def contacts(req: WSGIRequest):
    soc_netwrs = {
        'tel': '@XetPy',
        'vk': '@XetPy',
        'Телефон': '+79656650051'
    }
    return render(req, 'myapp/contacts.html', context={'infos': soc_netwrs})