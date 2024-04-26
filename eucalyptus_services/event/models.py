from django.db import models
from artist.models import Artist
import os
from django.conf import settings
from django.utils.text import slugify

def event_artwork_directory_path(instance, filename):
    # Obtain a clean artist name and create a path for the artwork
    # Uses 'slugify' to ensure file path compatibility
    base_filename, file_extension = os.path.splitext(filename)
    clean_artist_name = slugify(instance.artist.name)
    return f'artists/{clean_artist_name}/event/{base_filename}{file_extension}'

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artwork = models.ImageField(upload_to=event_artwork_directory_path)
    url = models.URLField()
    date_event = models.DateField
    location = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'