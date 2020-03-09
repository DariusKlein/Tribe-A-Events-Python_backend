from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
from events.models import Test_hub_model

# Create your views here.

def Event_read(response, url_id):
    print(url_id)
    event = Event.objects.get(id=url_id)
    html = "<h1>%s</h1>"  % event.title + \
            "<html><body>Test page <br> </body></html>" + \
            "<html><body>Naam: %s <br> </body></html>" % event.naam + \
            "<html><body>Beschrijving: %s <br> </body></html>" % event.beschrijving + \
            "<html><body>Begin Datum: %s <br> </body></html>" % event.begin_datum + \
            "<html><body>Eind Datum: %s <br> </body></html>" % event.eind_datum
    return HttpResponse(html)


def Test_hub_view(response):
    test_hub_object = Test_hub_model.objects.get(id=1)

    html = "<h1>%s</h1>"  % test_hub_object.title + \
            '<a href="/admin"> %s <br></a>' % test_hub_object.naam + \
            "<html><body>Events: %s <br> </body></html>" % Event.objects.count()
    for x in range (Event.objects.count()):
        x = x + 1
        print(x)
        event = Event.objects.get(id=x)
        html = html + "<html><body>%s) </body></html>" % x + \
               "<html><body>id: %s, </body></html>" % event.id + \
               "<html><body> Titel: %s, </body></html>" % event.title + \
               "<html><body> Naam: %s, </a>'</body></html>" % event.naam + \
               '<a href="/test/%s"> Meer informatie <br></a>' %x
    return HttpResponse(html)