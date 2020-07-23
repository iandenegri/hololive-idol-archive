from django.contrib import admin

from .models import Stream, Idol, Song, StreamTrack

# Register your models here.

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    filter_horizontal = ('songs',)
    list_display = ('name', 'singer', 'date_posted')
    list_filter = ('singer',)

admin.site.register(Idol)
admin.site.register(Song)
admin.site.register(StreamTrack)
