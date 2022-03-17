from django.db import models

class Produit(models.Model):
	id = models.IntegerField(primary_key=True, auto_created=True)
    designation = models.CharField(max_length=50)
    stock = models.IntegerField(max_length=11)
    prix_unitaire = models.IntegerField(max_length=11)

