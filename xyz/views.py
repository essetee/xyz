from gc import get_objects
from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Webpage


data = [ 
    {
        'topic': 'Linux',
        'titel': 'Ssh gebruiken zonder wachtwoord',
        'link': 'naam van de link is sshzonder.html'
    },
    {
        'topic': 'Raspberry',
        'titel': 'Overclocken van de pi4 en pi400',
        'link': 'naam van de link is overclock.html'
    },
    {
        'topic': 'FreeBSD',
        'titel': 'Werken met ports onder FreeBSD',
        'link': 'naam van de link is sshzonder.html'
    }
]


def home(request):
    data = Webpage.objects.all()
    return render(request, 'xyz/home.html', {'data': data })

def sitelinks(request):
    page = request.GET.get('p')
    return render(request, 'xyz/'+page,{})