from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['url','id','name','description','artist_logo','facebook','instagram','soundcloud','spotify','apple_music','tiktok','song_set']

class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'