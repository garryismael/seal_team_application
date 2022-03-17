from django.db import models

class Client(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)