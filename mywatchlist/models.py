
from django.db import models

class Myfavoritewatchlist(models.Model):
    review = models.TextField()
    watched = models.TextField()
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
