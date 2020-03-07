from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    naam = models.CharField(max_length=50)
    beschrijving = models.TextField()
    begin_datum = models.DateField()
    eind_datum = models.DateField()