from django.http import HttpResponseForbidden, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView, CreateView
from account_module.models import User
from channel_module.forms import EditProfileModelForm, PlaylistCreationForm
from post_module.models import Post, Playlist


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


class CreatePlaylistView(CreateView):
    model = Playlist
    form_class = PlaylistCreationForm
    template_name = 'Create_Playlist.html'
    success_url = reverse_lazy('home_page')

    def get_form_kwargs(self):
        kwargs = super(CreatePlaylistView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreatePlaylistView, self).get_context_data()
        current_user = User.objects.filter(id=self.request.user.id).first()
        context['current_user'] = current_user
        return context

    def form_valid(self, form):
        form.instance.channel = self.request.user
        form.instance.is_active = True
        response = super(CreatePlaylistView, self).form_valid(form)
        self.object.video.set(form.cleaned_data['video'])
        return response