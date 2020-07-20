import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse

now = timezone.now()

# Create your models here.


class Idol(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    jp_name = models.CharField(blank=True, null=True, max_length=264)
    channel = models.URLField(blank=True, unique=True)
    channel_id = models.CharField(blank=True, unique=True, max_length=264)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('archive:idol_detail', kwargs={'pk': self.pk})


class Song(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    romanji_name = models.CharField(blank=True, null=True, max_length=264)
    translated_name = models.CharField(blank=True, null=True, max_length=264)
    original_artist = models.CharField(blank=True, null=True, max_length=264)
    romanji_original_artist = models.CharField(blank=True, null=True, max_length=264)
    playlist_number = models.IntegerField(blank=True)


    def __str__(self):
        return self.name


class Stream(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    singer = models.ForeignKey(to=Idol, on_delete=models.CASCADE, blank=False)
    guest_singers = models.ManyToManyField(to=Idol, blank=True, related_name='guest_singers')
    link = models.URLField(blank=True, unique=True)
    youtube_id = models.CharField(blank=True, unique=True, max_length=264)
    songs = models.ManyToManyField(to=Song, blank=True)
    date_posted = models.DateField(blank=True, null=True, default=timezone.now)
    original_song = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('archive:stream_detail', kwargs={'pk': self.pk})
