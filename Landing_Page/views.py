from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
import datetime
from django.utils import timezone

def Startpagina(response):

    event_set = Event.objects.filter(begin_datum__gte=timezone.now().date()).order_by('begin_datum')

    html = "<h1>Event list</h1>" + \
            '<a href="/admin"> Admin page <br></a>' + \
            '<a href="/front"> Front-end demo page <br></a>' + \
            '<a href="/archief"> archief <br></a>' + \
            "<html><body>Events: %s <br> </body></html>" % Event.objects.count()

    for x in range (event_set.count()):
        event = event_set[x]
        x = x + 1
        html = html + "<html><body>%s) </body></html>" % x + \
               "<html><body> Titel: %s, <br></body></html>" % event.title + \
               "<html><body> begin datum: %s, </a>'</body></html>" % event.begin_datum + \
               '<a href="/%s"> Meer informatie <br></a>' %x
    return HttpResponse(html)