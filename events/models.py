from django.db import models

class Event(models.Model):
    Title = models.TextField()
    Naam = models.TextField()
    Beschrijving = models.TextField()
    Begin_datum = models.TextField()
    Eind_datum = models.TextField()