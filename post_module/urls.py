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
    path('post-like/<slug:slug>', views.BlogPostLike, name="post_like"),
    path('post-dislike/<slug:slug>', views.BlogPostDisLike, name="post_dislike"),

    # API Path
    # path('posts-apis/', views.PostListAPIView.as_view(), name='posts-Apiview'),
    # path('posts-update-apis/<int:pk>', views.PostRetrieveUpdateDestroy.as_view(), name='update'),
    #
    # path('posts-comments-apis/', views.PostCommentAPIView.as_view(), name='comments_apis'),
    # path('posts-comments-update-apis/<int:pk>', views.PostCommentRetrieveUpdateDestroy.as_view(), name='update_comment'),
    #
    # path('posts-playlists-apis/', views.PlaylistAPIView.as_view(), name='playlist_apis'),
    # path('posts-playlists-update-apis/<int:pk>', views.PlaylistRetrieveUpdateDestroy.as_view(), name='update_playlist'),
    #
    # path('posts-playlists-video-apis/', views.PlaylistVideoAPIView.as_view(), name='playlist_video_apis'),
    # path('posts-playlists-video-update-apis/<int:pk>', views.PlaylistVideoRetrieveUpdateDestroy.as_view(), name='update_playlist_video'),
]
