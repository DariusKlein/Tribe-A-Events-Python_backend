from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event


# Create your views here.

def index(response, url_id):
    print(url_id)
    event = Event.objects.get(id=url_id)
    return HttpResponse("<h1>%s</h1>" %event.naam)