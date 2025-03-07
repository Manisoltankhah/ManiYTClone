from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # user apis
    path('user-apis/', views.UserListAPIView.as_view(), name='user-api'),
    path('user-update-apis/<int:pk>', views.UserRetrieveUpdateDestroy.as_view(), name='user-api'),
    path('user-create-api/', views.CreateUserView.as_view(), name='user-create'),
    path('register-api/', views.UserRegisterAPIView.as_view(), name='register'),
    path('login-api/', views.UserLoginAPIView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='grt_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwNzQxMTAwLCJpYXQiOjE3NDA3NDA4MDAsImp0aSI6ImY2ZmZiOTQyMTI3YzRjODg4YWU1ODE2ZmUyNmZiZTc4IiwidXNlcl9pZCI6Nn0.bFC0QthLXX8WetbUNtQJWyJ9z2DIBAzeOm-opNqyHy4
    # post apis
    path('post-apis/', views.PostListAPIView.as_view(), name='posts-apis'),
    path('post-create-api/', views.PostListCreate.as_view(), name='posts-create'),
    path('post-delete-api/<int:pk>', views.PostDelete.as_view(), name='posts-delete'),
    path('post-update-apis/<int:pk>', views.PostRetrieveUpdateDestroy.as_view(), name='post-update'),


    path('post-comments-apis/', views.PostCommentAPIView.as_view(), name='comments_apis'),
    path('post-comments-create/', views.PostCommentListCreate.as_view(), name='comments_create'),
    path('post-comments-delete/<int:pk>', views.PostCommentDelete.as_view(), name='comments_delete'),
    path('post-comments-update-apis/<int:pk>', views.PostCommentRetrieveUpdateDestroy.as_view(), name='comment_update'),


    path('post-playlists-apis/', views.PlaylistAPIView.as_view(), name='playlist_apis'),
    path('post-playlist-create/', views.PlaylistListCreate.as_view(), name='playlist_create'),
    path('post-playlist-delete/<int:pk>', views.PlaylistDelete.as_view(), name='playlist_delete'),
    path('post-playlists-update-apis/<int:pk>', views.PlaylistRetrieveUpdateDestroy.as_view(), name='playlist-update'),


    path('post-playlists-video-apis/', views.PlaylistVideoAPIView.as_view(), name='playlist_video_apis'),
    path('post-playlists-video-create/', views.PlaylistVideoListCreate.as_view(), name='playlist_video_create'),
    path('post-playlists-video-delete/<int:pk>', views.PlaylistVideoDelete.as_view(), name='playlist_video_delete'),
    path('post-playlists-video-update-apis/<int:pk>', views.PlaylistVideoRetrieveUpdateDestroy.as_view(), name='playlist_video_update'),
]