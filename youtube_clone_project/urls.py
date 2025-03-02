"""youtube_clone_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from youtube_clone_project import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/' , include('api.urls'), name='api'),

    path('', include('home_module.urls')),
    path('', include('post_module.urls')),
    path('account/', include('account_module.urls')),
    path('channel/', include('channel_module.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('__debug__/', include(debug_toolbar.urls)),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
