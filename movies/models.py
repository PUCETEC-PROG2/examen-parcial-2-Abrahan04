
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.titl