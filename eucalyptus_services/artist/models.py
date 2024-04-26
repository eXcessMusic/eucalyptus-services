from django.db import models
import os
from django.conf import settings
from django.utils.text import slugify


#Custom MKDIR

""" def artist_directory_path(instance, filename):
    # Obtient un titre de film nettoyé et crée un chemin pour l'affiche
    # Utilise 'slugify' pour assurer la compatibilité du chemin de fichier
    base_filename, file_extension = os.path.splitext(filename)
    clean_title = slugify(instance.titre)
    return f'{base_filename}{file_extension}' """

# Create your models here.
def artist_logo_directory_path(instance, filename):
    # Obtain a clean artist name and create a path for the artwork
    # Uses 'slugify' to ensure file path compatibility
    base_filename, file_extension = os.path.splitext(filename)
    clean_artist_name = slugify(instance.artist.name)
    return f'artists/{clean_artist_name}/{base_filename}{file_extension}'
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    artist_logo = models.ImageField(upload_to=artist_logo_directory_path)
    facebook = models.URLField()
    instagram = models.URLField()
    soundcloud = models.URLField()
    spotify = models.URLField()
    apple_music = models.URLField()
    tiktok = models.URLField()

    def __str__(self):
        return f'{self.name}'

def song_artwork_directory_path(instance, filename):
    # Obtain a clean artist name and create a path for the artwork
    # Uses 'slugify' to ensure file path compatibility
    base_filename, file_extension = os.path.splitext(filename)
    clean_artist_name = slugify(instance.artist.name)
    return f'artists/{clean_artist_name}/{base_filename}{file_extension}'

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artwork = models.ImageField(upload_to=song_artwork_directory_path)
    soundcloud_url = models.URLField()
    spotify_url = models.URLField()
    applemusic_url = models.URLField()
    deezer_url = models.URLField()
    youtube_url = models.URLField()

    def __str__(self):
        return f'{self.name}'