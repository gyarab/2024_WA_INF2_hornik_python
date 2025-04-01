from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    formed_year = models.IntegerField()
    image_url = models.URLField(null=True)  # Přidání pole pro URL obrázku
    description = models.TextField(null=True, blank=True)  # Přidání pole pro popis kapely

    def __str__(self):
        return self.name

class Album(models.Model):
    band = models.ForeignKey(Band, related_name='albums', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    release_year = models.IntegerField()
    cover_image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
