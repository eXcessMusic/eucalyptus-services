from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
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

def add_success_message(request, message):
    messages.success(request, message)

def artist_list(request):
    query = request.GET.get('q', '')
    if query:
        artists = Artist.objects.filter(
            Q(name__icontains=query) | 
            Q(song__name__icontains=query)
        )
    else:
        artists = Artist.objects.all().order_by('id')
    
    artist_last_songs = []
    for artist in artists:
        last_song = Song.objects.filter(artist=artist).order_by('-id').first()
        artist_last_songs.append({'artists': artist, 'last_song': last_song})

    # Retrieve messages from the request
    all_messages = messages.get_messages(request)

    return render(request, 'artist/artist_list.html', {'artists': artist_last_songs, 'messages': all_messages})

def artist_detail(request, pk):
    artist = Artist.objects.get(pk=pk)
    last_song = Song.objects.filter(artist=artist).order_by('-id').first()
    return render(request, 'artist/artist_detail.html', {'artist': artist, 'last_song': last_song})

def artist_create(request):
    if request.method == 'POST':
        form = Create_artist_form(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            add_success_message(request, '💾 Artist successfully created!')
            return redirect('artist_list')
        
    # Retrieve messages from the request
    all_messages = messages.get_messages(request)

    return render(request, 'artist/artist_create.html', {'form': Create_artist_form, 'messages': all_messages})

@login_required
def artist_update(request, pk):
    artist = get_object_or_404(Artist, pk=pk)

    if request.method == 'POST':
        form = Update_artist_form(request.POST, request.FILES, instance=artist)

        if form.is_valid():
            form.save()
            add_success_message(request, '✍️ Artist infos successfully updated!')
            return redirect('artist_detail', pk=artist.id)
        else:
            # Print the validation errors for debugging
            print(form.errors)
    else:
        form = Update_artist_form(instance=artist)

    # Add this code to fetch the social media links from the database
    social_media_links = {
        'facebook': artist.facebook,
        'instagram': artist.instagram,
        'soundcloud': artist.soundcloud,
        'spotify': artist.spotify,
        'apple_music': artist.apple_music,
        'tiktok': artist.tiktok,
    }

    # Retrieve messages from the request
    all_messages = messages.get_messages(request)

    return render(request, 'artist/artist_update.html', {'form': form, 'social_media_links': social_media_links, 'messages': all_messages})

@login_required
def artist_delete(request, pk):    
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    add_success_message(request, '🫥 Artist successfully deleted!')
    return redirect('artist_list')

def artist_linkinbio(request, pk):
    artist = Artist.objects.get(pk=pk)
    context = {'artist': artist, 'songs': artist.song_set.all()}
    return render(request, 'artist/biolink.html', context)

@login_required
def song_create(request):
    if request.method == 'POST':
        form = Create_song_form(request.POST, request.FILES)
        if form.is_valid():
            if not request.user.is_superuser:
                form.instance.artist = request.user.artist
            form.save()
            add_success_message(request, '💿 Song successfully created!')
            return redirect('artist_list')
        else :
            print("Form is not valid")
        
    artist = Artist.objects.filter(associated_user=request.user).select_related('associated_user').first()
    return render(request, 'song/song_create.html', {'form': Create_song_form, 'artist': artist})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    artist = song.artist
    return render(request, 'song/song_detail.html', {'song': song, 'artist': artist})

@login_required
def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if song.artist.associated_user!= request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = Update_song_form(request.POST, request.FILES, instance=song)

        if form.is_valid():
            form.save()
            add_success_message(request, '✍️ Song successfully updated!')
            return redirect('artist_list')
    else:
        form = Update_song_form(instance=song)

    return render(request, 'song/song_update.html', {'form': form, 'song': song})

@login_required
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if song.artist.associated_user != request.user:
        return HttpResponseForbidden()

    song.delete()
    add_success_message(request, '🫥 Song successfully deleted!')
    return redirect('artist_list')

def song_list(request):
    songs = Song.objects.all()

    return render(request, 'song/song_list.html', {'songs': songs})