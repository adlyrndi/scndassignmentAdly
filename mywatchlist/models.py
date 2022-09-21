
from django.db import models

class Myfavoritewatchlist(models.Model):
    review = models.TextField()
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
