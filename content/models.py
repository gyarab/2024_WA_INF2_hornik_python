from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    formed_year = models.IntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.title
