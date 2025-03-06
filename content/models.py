from django.db import models

class Bands(models.Model):
    band = models.CharField(max_length=200)

class Album(models.Model):
    album = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=200)
    track_count = models.IntegerField()
    tracks = models.TextField()

    def __str__(self):
        return self.title