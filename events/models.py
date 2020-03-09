from django.db import models


class Event (models.Model):
    title = models.CharField(max_length=50)
    naam = models.CharField(max_length=50)
    beschrijving = models.TextField()
    begin_datum = models.DateField()
    eind_datum = models.DateField()


class Test_hub_model(models.Model):
    title = models.CharField(max_length=50)
    naam = models.CharField(max_length=50)

    #https: // docs.djangoproject.com / en / 3.0 / topics / db / models /