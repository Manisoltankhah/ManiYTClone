from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/home/', views.ChannelHomeView.as_view(), name='channel-home-page'),

]