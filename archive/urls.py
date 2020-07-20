from django.urls import path

from .views import StreamListView, StreamDetailView, StreamCreateView, StreamDeleteView, StreamUpdateView, \
    HomeView, IdolListView, IdolDetailView, IdolCreateView, IdolDeleteView, IdolUpdateView

app_name = 'archive'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('stream/', StreamListView.as_view(), name='stream_list'),
    path('stream/create/', StreamCreateView.as_view(), name='stream_create'),
    path('stream/<int:pk>/', StreamDetailView.as_view(), name='stream_detail'),
    path('stream/<int:pk>/update', StreamUpdateView.as_view(), name='stream_update'),
    path('stream/<int:pk>/delete', StreamDeleteView.as_view(), name='stream_delete'),
    path('idol/', IdolListView.as_view(), name='idol_list'),
    path('idol/create/', IdolCreateView.as_view(), name='idol_create'),
    path('idol/<int:pk>/', IdolDetailView.as_view(), name='idol_detail'),
    path('idol/<int:pk>/delete', IdolDeleteView.as_view(), name='idol_delete'),
    path('idol/<int:pk>/update', IdolUpdateView.as_view(), name='idol_update'),
]