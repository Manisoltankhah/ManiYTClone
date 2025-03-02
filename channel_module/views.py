from django.shortcuts import render
from django.views.generic import TemplateView
from account_module.models import User
from post_module.models import Post


class ChannelHomeView(TemplateView):
    template_name = 'channel-page.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelHomeView, self).get_context_data()
        channel_slug = kwargs.get('slug')
        user = User.objects.filter(slug__iexact=channel_slug).first()
        channel_posts = Post.objects.filter(channel__slug__iexact=channel_slug).order_by('-created_date')
        context['channel_info'] = user
        context['channel_posts'] = channel_posts
        return context


