import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

now = timezone.now()

# Create your models here.


class Idol(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    jp_name = models.CharField(blank=True, null=True, max_length=264)
    channel = models.URLField(blank=True, unique=True)
    channel_id = models.CharField(blank=True, unique=True, max_length=264)

    thumbnail = models.URLField(null=True, blank=True)

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('archive:song_detail', kwargs={'pk': self.pk})


class Stream(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    singer = models.ForeignKey(to=Idol, on_delete=models.CASCADE, blank=False)
    guest_singers = models.ManyToManyField(to=Idol, blank=True, related_name='guest_singers')
    link = models.URLField(blank=True, unique=True)
    youtube_id = models.CharField(blank=True, unique=True, max_length=264)
    songs = models.ManyToManyField(to=Song, through='StreamTrack', blank=True)
    date_posted = models.DateField(blank=True, null=True, default=timezone.now)
    original_song = models.BooleanField(default=False)
    thumbnail = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.youtube_id)
        super(Stream, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('archive:stream_detail', kwargs={'slug': self.slug})
        

class StreamTrack(models.Model):
    stream = models.ForeignKey(to=Stream, on_delete=models.CASCADE)
    song = models.ForeignKey(to=Song, on_delete=models.CASCADE)
    position = models.IntegerField()
    timestamp = models.IntegerField(null=True, blank=True, help_text="This is the point in seconds at which this song occurs in a stream.")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.song.name + " - " + self.stream.name + " -  Song Number " + str(self.position)

    def convert_seconds_to_timestamp(self):
        if self.timestamp:
            return str(datetime.timedelta(seconds=self.timestamp))
        else:
            return ''
