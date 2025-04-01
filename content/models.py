from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    formed_year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='bands/')

    def __str__(self):
        return self.name

class Album(models.Model):
    band = models.ForeignKey(Band, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    tracks = models.TextField()

    def __str__(self):
        return self.title
