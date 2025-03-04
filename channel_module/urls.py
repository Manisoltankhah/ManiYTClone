from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/home/', views.ChannelHomeView.as_view(), name='channel-home-page'),
    path('<slug:slug>/user-panel/', views.UserPanelView.as_view(), name='user-panel-page'),
    path('<slug:slug>/playlist-create/', views.CreatePlaylistView.as_view(), name='playlist-create-page'),

]