from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artist import views

router = DefaultRouter()
router.register(r'artist', views.ArtistViewSet)
router.register(r'song', views.SongViewSet)


urlpatterns = [
    path('', views.artist_list, name="home"),
    path('api/', include(router.urls)),
    path('artist/list/', views.artist_list, name="artist_list"),
    path('artist/<int:pk>', views.artist_detail, name="artist_detail"),
    path('artist/<int:pk>/links', views.artist_linkinbio, name="artist_linkinbio"),
    path('artist/create/', views.artist_create, name="artist_create"),
    path('artist/update/<int:pk>', views.artist_update, name="artist_update"),
    path('artist/delete/<int:pk>', views.artist_delete, name="artist_delete"),
    path('song/create/', views.song_create, name="song_create"),
    path('song/<int:pk>', views.song_detail, name="song_detail"),
    path('song/update/<int:pk>', views.song_update, name="song_update"),
    path('song/delete/<int:pk>', views.song_delete, name="song_delete"),
    path('songs/', views.song_list, name="song_list")
]