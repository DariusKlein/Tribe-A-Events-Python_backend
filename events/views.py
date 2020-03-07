from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.

def index(id): #def index(response, id):
    ls = Event.objects.get(id=1)
    return HttpResponse("<h1>%s</h1>" %ls.name)