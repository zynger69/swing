"""blazt URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from index.views import *
from player.views import *
from bgm.views import *
from search.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home_view"),
    path('song/<int:pk>/<alb__name>/<name>/',player_view,name="player_view"),
    path('<int:pk>/<name>-<alb__name>-mp3-download/',player_view,name="player_view"),
    
    path('search/',csrf_exempt(search),name="search"),
    
    path("bgms/",bgm_home_view,name="bgm_home"),
    path("bgm/<int:pk>/<str:name_name>/<str:alb_name>",bgm_player_view,name="bgm_player"),
    path("bgm/<int:pk>/<str:name_name>-<str:alb_name>-ringtone-download",bgm_player_view,name="bgm_player2"),
    path("dbgm/<int:pk>",dbgm_view,name="dbgm"),
    
    path("download/<str:path>/",download_view,name="download"),
    
    path("sitemap/",sitemap_view,name="sitemap_view"),
    
    path('playlist/<int:pk>',playlist_view,name='playlist_view'),
    path('<slug:lang__name>/',lang_view,name="lang_view"),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
