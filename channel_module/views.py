from django.http import HttpResponseForbidden, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from channel_module.forms import EditProfileModelForm
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


class UserPanelView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'edit_form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user-panel.html', context)

    def post(self, request: HttpRequest, *args, **kwargs):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return redirect(reverse('channel-home-page', args=[current_user.slug]))

        context = {
            'edit_form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user-panel.html', context)


class CreatePlaylistView(View):
    def get(self):
        channel_slug = self.kwargs['slug']
        user = User.objects.filter(slug__iexact=channel_slug).first()
        current_user = User.objects.filter(id=self.request.user.id).first()
        edit_profile_form = EditProfileModelForm(instance=current_user)
        context = {'edit_profile_form': edit_profile_form,
                   'current_user': current_user,
                   'channel_info': user
        }
        return render(self.request, 'user-panel.html', context)

    def post(self):
        current_user = User.objects.filter(id=self.request.user.id).first()
        edit_profile_form = EditProfileModelForm(self.request.POST, self.request.FILES, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save(commit=True)
            return redirect(reverse('channel-home', args=[current_user.slug]))