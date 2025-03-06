from django.urls import path
from . import views

urlpatterns = [
    # Show details of Posts
    path('watch/<slug:slug>/', views.PostDetailPage.as_view(), name='post_detail_page'),

    # Show details of Playlist
    path('watch/playlist/<slug:slug>/<slug:video_slug>/', views.PlaylistDetailView.as_view(), name='playlist_detail_page'),

    # create post url
    path('create-post/', views.CreatePostView.as_view(), name='create_post_page'),

    # Add Edit Delete comment
    path('watch/add-comment-on/<slug:slug>/<int:pk>/', views.AddComment.as_view(), name='add_post_comment'),
    path('watch/edit-comment/<slug:slug>/<int:pk>/', views.comment_edit, name='edit_post_comment'),
    path('watch/delete-comment/<slug:slug>/<int:pk>/', views.delete_comment, name='delete_post_comment'),

    # Likes and Dislikes
    path('post-like/<slug:slug>', views.PostLike, name="post_like"),
    path('post-dislike/<slug:slug>', views.PostDisLike, name="post_dislike"),

    path('history/<slug:slug>', views.HistoryView.as_view(), name='history'),
]
