from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, MusicTrack, MusicAlbum
from . import serializers


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class MusicTrackViewSet(viewsets.ModelViewSet):
    queryset = MusicTrack.objects.all()
    serializer_class = serializers.MusicTrackSerializer


class MusicAlbumViewSet(viewsets.ModelViewSet):
    queryset = MusicAlbum.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'artist',)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return serializers.CreateMusicAlbumSerializer
        return serializers.ReadMusicAlbumSerializer


# """
# View for all albums of artist with given id
# """
# class ArtistsAlbumsView(generics.ListAPIView):
#     serializer_class = MusicAlbumSerializer

#     def get_queryset(self):
#         id = self.kwargs['id']
#         if id is not None:
#             return Artist.objects.get(id=id).musicalbum_set.all()
#         return MusicAlbum.objects.none()
    