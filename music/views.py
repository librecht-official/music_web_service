from rest_framework import viewsets, generics, views
from rest_framework.response import Response
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


class ExploreView(views.APIView):
    # authentication_classes = ...
    def get(self, request, format=None):
        """ Just a mock of some sort of recommendation system """
        albums = MusicAlbum.objects.all()
        # trending = 
        # popular = albums[6:]
        recommendations = serializers.ReadMusicAlbumSerializer(
            albums[:2], many=True, context={'request': request}
        )
        trending = serializers.ReadMusicAlbumSerializer(
            albums[2:6], many=True, context={'request': request}
        )
        popular = serializers.ReadMusicAlbumSerializer(
            albums[6:26], many=True, context={'request': request}
        )
        return Response({
            'recommendations': recommendations.data,
            'trending': trending.data,
            'popular': popular.data
        })


# """
# View for all albums of artist with given id
# """
# class ArtistsAlbumsView(generics.ListAPIView):
#      serializer_class = MusicAlbumSerializer

#      def get_queryset(self):
#            id = self.kwargs['id']
#            if id is not None:
#                 return Artist.objects.get(id=id).musicalbum_set.all()
#            return MusicAlbum.objects.none()
    