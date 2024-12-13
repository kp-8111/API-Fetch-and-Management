from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
