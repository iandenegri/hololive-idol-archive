from django.contrib import admin

from .models import Stream, Idol, Song, StreamTrack

# Register your models here.

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    filter_horizontal = ('songs',)
    list_display = ('name', 'singer', 'date_posted')
    list_filter = ('singer',)
    prepopulated_fields = {"slug": ("youtube_id",)}


@admin.register(Idol)
class IdolAdmin(admin.ModelAdmin):
    list_display = ('name', 'jp_name', 'group')
    list_filter = ('group',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Song)
admin.site.register(StreamTrack)
