from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, View, TemplateView

from account_module.models import User
from post_module.forms import PostCommentForm, PostCommentUpdateForm, PostCreatingForm
from post_module.models import Post, PostViews, PostComments, Playlist, PlaylistVideo
from tools.Http_service import get_user_ip


# Actual Views
class PostDetailPage(DetailView):
    model = Post
    template_name = 'post_detail_page.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailPage, self).get_context_data()
        post_comment_form = PostCommentForm()
        post = self.object
        current_user = self.request.user.id
        related_posts = Post.objects.filter(is_active=True)
        post_comments = PostComments.objects.filter(post_id=post.id)
        views_number = PostViews.objects.filter(post_id=post.id).count()

        # passing data to context
        context['current_user'] = current_user
        context['views_number'] = views_number
        context['related_posts'] = related_posts
        context['post_comments'] = post_comments
        context['post_comment_form'] = post_comment_form

        # views
        user_ip = get_user_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        had_been_visited = PostViews.objects.filter(ip__iexact=user_ip, post_id=post.id).exists()
        if not had_been_visited:
            new_view = PostViews(ip=user_ip, user_id=user_id, post_id=post.id)
            new_view.save()

        # Likes
        likes_connected = get_object_or_404(Post, slug=self.kwargs['slug'])
        liked = False
        if likes_connected.likes.filter(post__likes__about_user=self.request.user):
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked
        return context


class CreatePostView(View):
    def get(self, request):
        post_creating_form = PostCreatingForm()
        context = {'post_creating_form': post_creating_form}
        return render(request, 'post_creation_page.html', context)

    def post(self, request):
        post_creating_form = PostCreatingForm(request.POST or None, request.FILES)
        if post_creating_form.is_valid():
            new_post = post_creating_form.save(commit=False)
            new_post.channel = self.request.user
            new_post.is_active = True
            new_post.save()
            playlists = post_creating_form.cleaned_data.get('playlists', [])
            for playlist in playlists:
                playlist.video.add(new_post)

            return redirect('home_page')

        context = {'post_creating_form': post_creating_form}
        return render(request, 'post_creation_page.html', context)


class AddComment(CreateView):
    model = PostComments
    form_class = PostCommentForm
    template_name = 'post_detail_page.html'
    context_object_name = 'post_comment_form'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail_page', args=(self.kwargs['slug'],))


class PlaylistDetailView(DetailView):
    template_name = 'playlist.html'
    model = Playlist
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super(PlaylistDetailView, self).get_context_data()
        current_video: Post = Post.objects.filter(slug=self.kwargs.get('video_slug')).first()
        current_video_comments = current_video.postcomments_set.prefetch_related('post__postcomments_set__user').all()
        print(current_video_comments)
        context['current_video'] = current_video
        context['current_video_comments'] = current_video_comments
        return context


def PostLike(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    if post.dislike.filter(id=request.user.id).exists():
        post.dislike.remove(request.user)
    return HttpResponseRedirect(reverse('post_detail_page', args=[str(slug)]))


def PostDisLike(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.dislike.filter(id=request.user.id).exists():
        post.dislike.remove(request.user)
    else:
        post.dislike.add(request.user)
    # delete like if user wants to dislike
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail_page', args=[str(slug)]))
    

def comment_edit(request, slug, pk):
    comment = get_object_or_404(PostComments, pk=pk)

    if request.method == 'POST':
        form = PostCommentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail_page', slug)
    else:
        form = PostCommentUpdateForm(instance=comment)

    return render(request, 'edit-comment-page.html', context={'form': form})


def delete_comment(request, pk, slug):
    comment = get_object_or_404(PostComments, pk=pk)
    if request.user.id == comment.user_id:
        PostComments.objects.get(pk=pk).delete()
    return redirect('post_detail_page', slug=slug)


class HistoryView(TemplateView):
    template_name = 'History.html'

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data()
        current_user = self.request.user
        if current_user.is_authenticated:
            viewed_posts = PostViews.objects.filter(user=current_user).prefetch_related('post__postviews_set', 'post__likes', 'post__dislike')
            liked_posts = Post.objects.filter(likes=current_user).prefetch_related('likes')
            comment_posts = PostComments.objects.filter(user=current_user).prefetch_related('post__postcomments_set')
            commented_on_post = [comment.post for comment in comment_posts]
            posts = [view.post for view in viewed_posts]
            context['posts'] = posts
            context['liked_posts'] = liked_posts
            context['commented_on_post'] = commented_on_post
        else:
            context['posts'] = []
        return context







