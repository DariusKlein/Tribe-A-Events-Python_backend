from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import serializer


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


def archief(response):

    event_archief = Event.objects.filter(begin_datum__lt=timezone.now().date()).order_by('begin_datum')

    html = "<h1>event archief</h1>" + \
            "<html><body>Events: %s <br> </body></html>" % event_archief.count()

    for x in range(event_archief.count()):

        event = event_archief[x]
        x = x + 1
        html = html + "<html><body>%s) </body></html>" % event.id + \
               "<html><body> Titel: %s, <br></body></html>" % event.title + \
               "<html><body> begin datum: %s, </a>'</body></html>" % event.begin_datum + \
               '<a href="/%s"> Meer informatie <br></a>' %event.id
    return HttpResponse(html)


class Testlistview(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = serializer


class TestDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = serializer