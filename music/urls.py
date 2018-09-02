from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'music_tracks', views.MusicTrackViewSet)
router.register(r'music_albums', views.MusicAlbumViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    # path('artists/<int:id>/music_albums', views.ArtistsAlbumsView.as_view()),
]