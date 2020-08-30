def set_to_karaoke(modeladmin, request, queryset):
    queryset.update(stream_type='Karaoke Stream')
set_to_karaoke.short_description = "Mark selected videos as Karaoke Streams"

def set_to_cover(modeladmin, request, queryset):
    queryset.update(stream_type='Original Song')
set_to_cover.short_description = "Mark selected videos as Original Songs"

def set_to_original(modeladmin, request, queryset):
    queryset.update(stream_type='Cover')
set_to_original.short_description = "Mark selected videos as Covers"

