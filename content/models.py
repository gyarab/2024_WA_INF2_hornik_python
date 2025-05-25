from django.db import models
from datetime import timedelta

class Band(models.Model):
    name = models.CharField(max_length=100)
    founded = models.CharField(max_length=100, blank=True, null=True)
    genre = models.ManyToManyField('Genre', related_name="bands", blank=True)
    description = models.TextField()
    logo = models.URLField(max_length=500, blank=True, null=True)
    photo = models.URLField(max_length=500, blank=True, null=True)
    members = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    band = models.ForeignKey(Band, related_name='album', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.IntegerField(null=True, blank=True)
    cover_image = models.URLField(max_length=500, blank=True, null=True)
    track_count = models.PositiveIntegerField(null=True, blank=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def track_count(self):
        return self.songs.count()
    
    @property
    def total_duration(self):
        durations = [song.duration for song in self.songs.all() if song.duration]
        total = sum(durations, timedelta())
        minutes, seconds = divmod(total.total_seconds(), 60)
        return f"{int(minutes):02}:{int(seconds):02}"

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.title
    