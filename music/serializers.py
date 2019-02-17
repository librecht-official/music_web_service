from rest_framework import serializers
from .models import Artist, MusicTrack, MusicAlbum


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class MusicTrackSerializer(serializers.ModelSerializer):
    audio = serializers.FileField()

    class Meta:
        model = MusicTrack
        fields = ('id', 'title', 'durationSec', 'albums', 'audio')


class ReadMusicAlbumSerializer(serializers.ModelSerializer):
    tracks = MusicTrackSerializer(many=True)
    artist = ArtistSerializer()
    coverImage = serializers.ImageField()

    class Meta:
        model = MusicAlbum
        fields = ('id', 'title', 'artist', 'tracks', 'coverImage')


class CreateMusicAlbumSerializer(serializers.ModelSerializer):
    # tracks = MusicTrackSerializer(many=True)
    coverImage = serializers.ImageField()

    class Meta:
        model = MusicAlbum
        fields = ('id', 'title', 'artist', 'tracks', 'coverImage')

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = MusicAlbum.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         MusicTrack.objects.create(album=album, **track_data)
    #     return album
