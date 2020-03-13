from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
import datetime
from django.utils import timezone

# Create your views here.

def Event_read(response, url_id):
    print(url_id)
    event = Event.objects.get(id=url_id)
    html = "<h1>%s</h1>"  % event.title + \
            "<html><body>Test page <br> </body></html>" + \
            "<html><body>Naam: %s <br> </body></html>" % event.naam + \
            "<html><body>Beschrijving: %s <br> </body></html>" % event.beschrijving + \
            "<html><body>Begin Datum: %s <br> </body></html>" % event.begin_datum + \
            "<html><body>Eind Datum: %s <br> </body></html>" % event.eind_datum + \
            "<html><body>Start Tijd: %s <br> </body></html>" % event.start_tijd + \
            "<html><body>Eind Tijd: %s <br> </body></html>" % event.eind_tijd

    return HttpResponse(html)


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
               '<a href="/test/%s"> Meer informatie <br></a>' %x
    return HttpResponse(html)


def archief(response):

    event_archief = Event.objects.filter(begin_datum__lt=timezone.now().date()).order_by('begin_datum')

    html = "<h1>event archief</h1>" + \
            "<html><body>Events: %s <br> </body></html>" % Event.objects.count()

    for x in range (event_archief.count()):

        event = event_archief[x]
        x = x + 1
        html = html + "<html><body>%s) </body></html>" % x + \
               "<html><body> Titel: %s, <br></body></html>" % event.title + \
               "<html><body> begin datum: %s, </a>'</body></html>" % event.begin_datum + \
               '<a href="/test/%s"> Meer informatie <br></a>' %x
    return HttpResponse(html)


