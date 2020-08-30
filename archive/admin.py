from django.contrib import admin

from .models import Stream, Idol, Song, StreamTrack
from .utils import set_to_karaoke, set_to_cover, set_to_original

# Register your models here.

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    filter_horizontal = ('songs',)
    list_display = ('name', 'singer', 'date_posted', 'stream_type')
    list_filter = ('singer', 'stream_type',)
    prepopulated_fields = {"slug": ("youtube_id",)}
    actions = [set_to_karaoke, set_to_cover, set_to_original]


@admin.register(Idol)
class IdolAdmin(admin.ModelAdmin):
    list_display = ('name', 'jp_name', 'group')
    list_filter = ('group',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Song)
admin.site.register(StreamTrack)
