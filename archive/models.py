import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

now = timezone.now()

# Create your models here.

# TODO: FIX THE ORDERING OF THIS AND THEN FIX INSTANCES IN TEMPLATE THAT SHOW THIS.
AGENCY_CHOICES = (
    ("Nijisanji", "NIJISANJI"),
    ("Hololive", "HOLOLIVE"),
    ("Independent", "INDIE"),
    ("774 inc.", "774")
)

SUBGROUP_CHOICES = (
    ("Hololive First Generation", "FIRST"),
    ("Hololive Second Generation", "SECOND"),
    ("Hololive Third Generation", "THIRD"),
    ("Hololive Fourth Generation", "FOURTH"),
    ("Hololive Fifth Generation", "FIFTH"),
    ("Hololive Gamers", "GAMER"),
    ("Hololive 3D Talent", "3D"),
    ("Hololive 2D Talent", "2D"),
    ("INoNaKa MUSIC", "INoNaKa"),
)

STREAM_TYPE_CHOICES = (
    ("KARAOKE", "Karaoke Stream"),
    ("ORIGINAL", "Original Song"),
    ("COVER", "Cover"),
)

class Singer(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    jp_name = models.CharField(blank=True, null=True, max_length=264)
    channel = models.URLField(blank=True, unique=True)
    channel_id = models.CharField(blank=True, unique=True, max_length=264)
    slug = models.SlugField()
    twitter = models.URLField(blank=True)
    agency = models.CharField(blank=True, max_length=256, choices=AGENCY_CHOICES)
    subgroup = models.CharField(blank=True, max_length=256, choices=SUBGROUP_CHOICES)

    thumbnail = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Singer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('archive:singer_detail', kwargs={'slug': self.slug})


class Song(models.Model):
    name = models.CharField(blank=False, max_length=264)
    romanji_name = models.CharField(blank=True, null=True, max_length=264)
    translated_name = models.CharField(blank=True, null=True, max_length=264)
    original_artist = models.CharField(blank=True, null=True, max_length=264)
    romanji_original_artist = models.CharField(blank=True, null=True, max_length=264)

    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Song, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('archive:song_detail', kwargs={'slug': self.slug})


class Stream(models.Model):
    name = models.CharField(blank=False, null=False, max_length=264)
    singer = models.ForeignKey(to=Singer, on_delete=models.CASCADE, blank=False)
    guest_singers = models.ManyToManyField(to=Singer, blank=True, related_name='guest_singers')
    link = models.URLField(blank=False, unique=True)
    youtube_id = models.CharField(blank=False, unique=True, max_length=264)
    songs = models.ManyToManyField(to=Song, through='StreamTrack', blank=True)
    date_posted = models.DateField(blank=True, null=True, default=timezone.now)
    stream_type = models.CharField(blank=True, max_length=256, choices=STREAM_TYPE_CHOICES)
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
