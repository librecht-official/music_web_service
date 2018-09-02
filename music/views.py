from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, MusicTrack, MusicAlbum
from .serializers import ArtistSerializer, MusicTrackSerializer, MusicAlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class MusicTrackViewSet(viewsets.ModelViewSet):
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer


class MusicAlbumViewSet(viewsets.ModelViewSet):
    queryset = MusicAlbum.objects.all()
    serializer_class = MusicAlbumSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'artist',)

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
    