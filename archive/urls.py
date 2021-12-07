from django.urls import path

from .views import *

app_name = 'archive'
urlpatterns = [
    # GENERIC
    path('', HomeView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('administration/login/', LoginUser.as_view(), name='admin_login'),
    path('administration/logout/', LogoutUser.as_view(), name='admin_logout'),
    path('about/', AboutView.as_view(), name='about'),
    # STREAM
    path('stream/', StreamListView.as_view(), name='stream_list'),
    path('stream/create/', StreamCreateView.as_view(), name='stream_create'),
    path('stream/<slug>/', StreamDetailView.as_view(), name='stream_detail'),
    path('stream/<slug>/update', StreamUpdateView.as_view(), name='stream_update'),
    path('stream/<slug>/delete', StreamDeleteView.as_view(), name='stream_delete'),
    # SINGER
    path('singer/', SingerListView.as_view(), name='singer_list'),
    path('singer/create/', SingerCreateView.as_view(), name='singer_create'),
    path('singer/<slug>/', SingerDetailView.as_view(), name='singer_detail'),
    path('singer/<slug>/delete', SingerDeleteView.as_view(), name='singer_delete'),
    path('singer/<slug>/update', SingerUpdateView.as_view(), name='singer_update'),
    # SONG
    path('song/create/', SongCreateView.as_view(), name='song_create'),
    path('song/<str:slug>/', SongDetailView.as_view(), name='song_detail'),
]