from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', related_name="bands", blank=True)
    description = models.TextField()
    logo = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    band = models.ForeignKey(Band, related_name='album', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.IntegerField(null=True, blank=True)
    cover_image = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name