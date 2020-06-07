from django.db import models


class Event (models.Model):
    title = models.CharField(max_length=50)
    naam = models.CharField(max_length=50)
    beschrijving = models.TextField()
    begin_datum = models.DateField()
    eind_datum = models.DateField()
    start_tijd = models.TimeField(default='00:00')
    eind_tijd = models.TimeField(default='23:59')


    #https: // docs.djangoproject.com / en / 3.0 / topics / db / models /