from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
import datetime

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


def Test_hub_view(response):

    test_hub_object = Test_hub_model.objects.get(id=1)

    html = "<h1>Event list</h1>" + \
            '<a href="/admin"> Admin page <br></a>' + \
            "<html><body>Events: %s <br> </body></html>" % Event.objects.count()

    for x in range (Event.objects.count()):
        x = x + 1
        print(x)
        event = Event.objects.get(id=x)

        html = html + "<html><body>%s) </body></html>" % x + \
               "<html><body> Titel: %s, <br></body></html>" % event.title + \
               "<html><body> begin datum: %s, </a>'</body></html>" % event.begin_datum + \
               '<a href="/test/%s"> Meer informatie <br></a>' %x
    return HttpResponse(html)