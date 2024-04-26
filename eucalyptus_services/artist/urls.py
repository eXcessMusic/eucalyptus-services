from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'song', SongViewSet)


urlpatterns = [
    path('', include(router.urls))
]