from django.urls import path
from home_module import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='home_page'),
]