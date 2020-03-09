from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event


# Create your views here.

def index(response, url_id):
    print(url_id)
    event = Event.objects.get(id=url_id)
    html1 = "<h1>%s</h1>"  % event.title + \
            "<html><body>Test page <br> </body></html>" + \
            "<html><body>Naam: %s <br> </body></html>" % event.naam + \
            "<html><body>Beschrijving: %s <br> </body></html>" % event.beschrijving + \
            "<html><body>Begin Datum: %s <br> </body></html>" % event.begin_datum + \
            "<html><body>Eind Datum: %s <br> </body></html>" % event.eind_datum
    return HttpResponse(html1)