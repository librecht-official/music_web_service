from __future__ import unicode_literals
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=63, null=False)

    def __str__(self):
        return '{}'.format(self.name)


class MusicTrack(models.Model):
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '{}'.format(self.title)


class MusicAlbum(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    tracks = models.ManyToManyField(MusicTrack)
    coverImage = models.ImageField(upload_to='images/music_album_covers', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.artist.name)
