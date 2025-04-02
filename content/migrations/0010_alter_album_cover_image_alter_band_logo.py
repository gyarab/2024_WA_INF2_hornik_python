# Generated by Django 5.1.6 on 2025-04-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_band_founded_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='band',
            name='logo',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
