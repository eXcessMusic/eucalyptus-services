from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

# class Create_article_form(forms.Form):
#     titre = forms.CharField(max_length=100)
#     # reste des autres propriétés

class Create_artist_form(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class Update_artist_form(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class Create_song_form(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'artist', 'artwork', 'soundcloud_url', 'spotify_url', 'applemusic_url', 'deezer_url', 'youtube_url')
        widgets = {
            'artwork': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class Update_song_form(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'