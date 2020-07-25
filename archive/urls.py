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
    path('stream/<int:pk>/', StreamDetailView.as_view(), name='stream_detail'),
    path('stream/<int:pk>/update', StreamUpdateView.as_view(), name='stream_update'),
    path('stream/<int:pk>/delete', StreamDeleteView.as_view(), name='stream_delete'),
    # IDOL
    path('idol/', IdolListView.as_view(), name='idol_list'),
    path('idol/create/', IdolCreateView.as_view(), name='idol_create'),
    path('idol/<int:pk>/', IdolDetailView.as_view(), name='idol_detail'),
    path('idol/<int:pk>/delete', IdolDeleteView.as_view(), name='idol_delete'),
    path('idol/<int:pk>/update', IdolUpdateView.as_view(), name='idol_update'),
    # SONG
    path('song/create/', SongCreateView.as_view(), name='song_create'),
    path('song/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
]