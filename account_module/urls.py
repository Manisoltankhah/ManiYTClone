from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.RegisterView.as_view(), name='sign_up'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    # path('user-apis/', views.UserListAPIView.as_view(), name='user-api'),
    # path('user-apis/<int:pk>', views.UserRetrieveUpdateDestroy.as_view(), name='user-api'),
]