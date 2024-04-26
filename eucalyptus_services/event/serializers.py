from rest_framework import serializers
from .models import *
from ..artist.models import Artist

class EventSerializer(serializers.HyperlinkedModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Artist.objects.all(),
        write_only=True,
        source='artist'
    )
    artist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='artist-detail'
    )

    class Meta:
        model = Event
        fields = ['url','id', 'name', 'artwork', 'url', 'date_event', 'location']