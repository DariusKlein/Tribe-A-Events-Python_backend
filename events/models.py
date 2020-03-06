from django.db import models

class Event(models.Model):
    title = models.TextField()
    naam = models.TextField()
    beschrijving = models.TextField()
    begin_datum = models.TextField()
    eind_datum = models.TextField()