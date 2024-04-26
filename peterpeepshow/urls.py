"""
URL configuration for peterpeepshow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.user_signup),
    path('home/',views.home , name='home'),
    path('login/',views.login , name='login'),
    path('admovies/',views.admovies),
    
    # Movies pages
    path('m1/',views.m_display),
    path('home/m_display.html',views.home),
    # Genres
    path('home/genres.html',views.genres),
    path('home/g_action.html',views.g_action),
    path('home/g_advanture.html',views.g_advanture),
    path('home/g_comedy.html',views.g_comedy),
    path('home/g_doc.html',views.g_doc),
    path('home/g_drama.html',views.g_drama),
    path('home/g_horror.html',views.g_horror),
    path('home/g_romance.html',views.g_romance),
    path('home/g_sifi.html',views.g_sifi),
    path('home/g_thriller.html',views.g_thriller),


    path('home/anime.html',views.anime),
    path('home/tvshow.html',views.tvshows),
    path('home/about.html',views.about),
    path('home/news.html',views.news),


    path('addgonor/',views.adgonor),

    path('m_display/', views.m_display, name='m_display'),
]