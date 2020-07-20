# Python
import os

# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Stream, Idol

# Third Party
from googleapiclient.discovery import build

youtube_api_key = os.environ.get('YOUTUBE_KEY', 'replace_me')
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Create your views here.


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_streams'] = Stream.objects.all().order_by('pk')[:5]
        return context

#######################################
# STREAM VIEWS
#######################################

class StreamListView(ListView):

    template_name = 'stream_list.html'
    model = Stream
    context_object_name = 'stream_list'
    paginate_by = 10

class StreamDetailView(DetailView):

    template_name = 'stream_detail.html'
    model = Stream
    context_object_name = 'stream'

class StreamCreateView(CreateView):

    template_name = 'stream_create.html'
    model = Stream
    fields = '__all__'

class StreamDeleteView(DeleteView):

    model = Stream
    success_url = reverse_lazy('archive:stream_list')
    template_name = 'stream_delete.html'

class StreamUpdateView(UpdateView):
    model = Stream
    fields = '__all__'
    template_name = 'stream_update.html'

#######################################
# IDOL VIEWS
#######################################

class IdolListView(ListView):

    template_name = 'idol_list.html'
    model = Idol
    context_object_name = 'idol_list'
    paginate_by = 10
    queryset = Idol.objects.all().order_by('name')


class IdolDetailView(DetailView):

    template_name = 'idol_detail.html'
    model = Idol
    context_object_name = 'idol'

    def get_context_data(self, **kwargs):
        idol_to_look_up = Idol.objects.get(pk=self.kwargs['pk'])
        try:
            youtube = build('youtube', 'v3', developerKey=youtube_api_key)

            request = youtube.channels().list(
                part="snippet,contentDetails,statistics",
                id=idol_to_look_up.channel_id
            )
            response = request.execute()

            context = super().get_context_data(**kwargs)

            context['subscribers'] = response['items'][0]['statistics']['subscriberCount']
            context['thumbnail_url'] = response['items'][0]['snippet']['thumbnails']['high']['url']
        except Exception as e:
            print(e)
            context['subscribers'] = 'N/A'
            context['thumbnail_url'] = 'https://pbs.twimg.com/profile_images/1186979284319006720/gH6xdlYB_400x400.jpg'

        return context


class IdolCreateView(CreateView):

    template_name = 'idol_create.html'
    model = Idol
    fields = '__all__'


class IdolDeleteView(DeleteView):

    model = Idol
    success_url = reverse_lazy('archive:idol_list')
    template_name = 'idol_delete.html'

class IdolUpdateView(UpdateView):

    model = Idol
    fields = '__all__'
    template_name = 'idol_update.html'
