# Generated by Django 5.1.6 on 2025-04-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_rename_cover_album_cover_image_url_remove_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
