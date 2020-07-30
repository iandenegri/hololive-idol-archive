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
    # IDOL
    path('idol/', IdolListView.as_view(), name='idol_list'),
    path('idol/create/', IdolCreateView.as_view(), name='idol_create'),
    path('idol/<slug>/', IdolDetailView.as_view(), name='idol_detail'),
    path('idol/<slug>/delete', IdolDeleteView.as_view(), name='idol_delete'),
    path('idol/<slug>/update', IdolUpdateView.as_view(), name='idol_update'),
    # SONG
    path('song/create/', SongCreateView.as_view(), name='song_create'),
    path('song/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
]