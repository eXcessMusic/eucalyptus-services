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

class Update_artist_form(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description', 'artist_logo', 'facebook', 'instagram', 'soundcloud', 'spotify', 'apple_music', 'tiktok', 'associated_user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(Update_artist_form, self).__init__(*args, **kwargs)
        if self.request and not self.request.user.is_superuser:
            self.fields['associated_user'].initial = self.request.user.id

    def save(self, commit=True):
        artist = super().save(commit=False)
        if commit:
            artist.save()
        return artist

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