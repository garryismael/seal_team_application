from django.db import models

class Client(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
