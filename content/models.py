from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    formed_year = models.IntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="albums", null=True)
    title = models.CharField(max_length=255, null=True)
    release_year = models.IntegerField()
    cover = models.URLField(null=True, blank=True)  # URL to the album cover image
    
    def __str__(self):
        return f"{self.title} - {self.band.name}"

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")
    title = models.CharField(max_length=255, null=True)
    duration = models.TimeField()

    def __str__(self):
        return self.title
