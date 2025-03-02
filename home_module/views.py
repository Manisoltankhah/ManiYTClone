from django.db.models import Count, OuterRef, Subquery
from django.shortcuts import render
from django.views.generic import TemplateView
from post_module.models import Post, PostViews, Playlist, PlaylistVideo


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data()
        posts = Post.objects.filter(is_active=True).order_by('-created_date')[:10]
        playlists = Playlist.objects.filter(is_active=True).order_by('-created_date')[:10]

        for playlist in playlists:
            thumbnail = playlist.video.first().thumbnail.url
            playlist.thumbnail_url = playlist.video.first().thumbnail.url
        playlists = playlists
        most_viewed_posts = Post.objects.annotate(view_count=Count('postviews')).order_by('-view_count').filter(is_active=True, view_count__gt=0)[:10]
        context['playlists'] = playlists
        context['most_viewed_posts'] = most_viewed_posts
        context['posts'] = posts
        return context


def site_header_partial(request):
    return render(request, 'site_header_partial.html', {})

