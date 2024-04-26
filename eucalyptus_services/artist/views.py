from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
# class ArtistList(generics.ListCreateAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
    
# class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
#     # Permet de bloquer l'accès au PUT/DELETE si l'utilisateur n'est pas authentifié ou admin
#     # permission_classes = [IsAuthenticatedOrReadOnly]

#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# class SongList(generics.ListCreateAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer