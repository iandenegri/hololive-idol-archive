# Python
import os

# Django
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Stream, Singer, Song

# Third Party
from googleapiclient.discovery import build

youtube_api_key = os.environ.get("YOUTUBE_KEY", "you need a youtube api key")
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Create your views here.


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_streams'] = Stream.objects.order_by('-date_posted')[:3]
        return context


class LoginUser(LoginView):
    
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('archive:index')


class LogoutUser(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('archive:index')


class AboutView(TemplateView):

    template_name = 'about.html'


# TODO: Revamp this to be more broken up. A lot of stuff lives here that can live in utils.py
class SearchResultsView(TemplateView):

    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q')
        if search_query == '':
            self.stream_song_results = ''
            self.stream_results = ''
            self.song_results = ''
            return super().get(request, *args, **kwargs)

        # STREAM SONG SEARCH UTIL
        try:
            # Streams containing songs that match that result
            self.stream_song_results = Stream.objects.filter(
                Q(streamtrack__song__name__icontains=search_query) | \
                Q(streamtrack__song__romanji_name__icontains=search_query) | \
                Q(streamtrack__song__translated_name__icontains=search_query)
            )[:5]
            print(self.stream_song_results)
        except Exception as e:
            print(e)
            self.stream_song_results = ''
        
        # STREAM SEARCH UTIL
        try:
            # Streams that match that result
            self.stream_results = Stream.objects.filter(
                Q(name__icontains=search_query) | \
                Q(singer__name__icontains=search_query) | \
                Q(singer__jp_name__icontains=search_query)
            )[:5]
        except Exception as e:
            print(e)
            self.stream_results = ''

        # SONG SEARCH UTIL
        try:
            # Songs that match that result
            self.song_results = Song.objects.filter(
                Q(name__icontains=search_query) | \
                Q(romanji_name__icontains=search_query) | \
                Q(translated_name__icontains=search_query) | \
                Q(original_artist__icontains=search_query) | \
                Q(romanji_original_artist__icontains=search_query)
            )[:5]
        except Exception as e:
            print(e)
            self.song_results = ''

        # SINGER SEARCH UTIL
        # Todo: see above

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            stream_song_results=self.stream_song_results,
            stream_results=self.stream_results,
            song_results=self.song_results,
            # singer_results=self.singer_results
            **kwargs)

#######################################
# STREAM VIEWS
#######################################


class StreamListView(ListView):

    template_name = 'stream_list.html'
    model = Stream
    context_object_name = 'stream_list'
    paginate_by = 15
    ordering = ['-date_posted']

    def get_queryset(self):
        print(self.request.GET)
        print(len(self.request.GET))
        if len(self.request.GET) > 0:
            if self.request.GET.get('stream_type', False):
                qs = Stream.objects.filter(active=True, stream_type=self.request.GET.get('stream_type')).order_by('-date_posted')
            else:
                qs = Stream.objects.filter(active=True)
            if self.request.GET.get('order_by', False):
                qs = qs.order_by(self.request.GET.get('order_by'))
            else:
                qs = qs.order_by('-date_posted')
        else:
            qs = Stream.objects.filter(active=True).order_by('-date_posted')
        return qs

class StreamDetailView(DetailView):

    template_name = 'stream_detail.html'
    model = Stream
    context_object_name = 'stream'

    def get_object(self):
        obj = super().get_object()
        if obj.thumbnail:
            print("This stream already has a thumbnail, don't fetch.")
            pass
        else:
            print('doing the thing')
            try:
                youtube = build('youtube', 'v3', developerKey=youtube_api_key)

                request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=obj.youtube_id
                )
                response = request.execute()
                obj.thumbnail = response['items'][0]['snippet']['thumbnails']['high']['url']
            except Exception as e:
                print(e)
                obj.thumbnail = 'https://pbs.twimg.com/profile_images/1186979284319006720/gH6xdlYB_400x400.jpg'
            obj.save()
        return obj


@method_decorator(login_required, name='dispatch')
class StreamCreateView(CreateView):

    template_name = 'stream_create.html'
    model = Stream
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class StreamDeleteView(DeleteView):

    model = Stream
    success_url = reverse_lazy('archive:stream_list')
    template_name = 'stream_delete.html'


@method_decorator(login_required, name='dispatch')
class StreamUpdateView(UpdateView):
    model = Stream
    fields = '__all__'
    template_name = 'stream_update.html'


#######################################
# SINGER VIEWS
#######################################


class SingerListView(ListView):

    template_name = 'singer_list.html'
    model = Singer
    context_object_name = 'singer_list'
    paginate_by = 100
    queryset = Singer.objects.all().order_by('name')


class SingerDetailView(DetailView):

    template_name = 'singer_detail.html'
    model = Singer
    context_object_name = 'singer'

    def get_object(self):
        obj = super().get_object()
        print(obj)
        if obj.thumbnail:
            print("This stream already has a thumbnail, don't fetch.")
            pass
        else:
            try:
                youtube = build('youtube', 'v3', developerKey=youtube_api_key)

                request = youtube.channels().list(
                    part="snippet,contentDetails,statistics",
                    id=obj.channel_id
                )
                response = request.execute()
                obj.thumbnail = response['items'][0]['snippet']['thumbnails']['high']['url']
            except Exception as e:
                print(e)
                obj.thumbnail = 'https://pbs.twimg.com/profile_images/1186979284319006720/gH6xdlYB_400x400.jpg'
            obj.save()
        return obj


@method_decorator(login_required, name='dispatch')
class SingerCreateView(CreateView):

    template_name = 'singer_create.html'
    model = Singer
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class SingerDeleteView(DeleteView):

    model = Singer
    success_url = reverse_lazy('archive:singer_list')
    template_name = 'singer_delete.html'


@method_decorator(login_required, name='dispatch')
class SingerUpdateView(UpdateView):

    model = Singer
    fields = '__all__'
    template_name = 'singer_update.html'


#######################################
# SONG VIEWS
#######################################


class SongCreateView(CreateView):

    model = Song
    template_name = 'song_create.html'
    fields = '__all__'


class SongDetailView(DetailView):

    template_name = 'song_detail.html'
    model = Song
    context_object_name = 'song'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streams_with_song'] = Stream.objects.filter(Q(streamtrack__song__slug=self.kwargs['slug']))
        return context
