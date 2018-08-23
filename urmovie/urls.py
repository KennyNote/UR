"""UR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from urmovie.views import main_view,movie_view,actor_view,contact_view

"""
    URMovie应用下的路由系统
"""
urlpatterns = [
    path('', main_view.index),
    path('index', main_view.index),
    path('movie_class', main_view.movie_class),
    path('actor_class', main_view.actor_class),
    path('contact', main_view.contact),
    url(r'^recommend-(?P<name>\d+)',movie_view.recommend),
    url(r'^queryMovieByAge-(?P<age>\d+)-(?P<pageid>\d+)',movie_view.queryMovieByAge),
    url(r'^queryMovieByCate-(?P<cate>\d+)-(?P<pageid>\d+)',movie_view.queryMovieByCate),
    url(r'^queryMovie-(?P<id>\d+)',movie_view.queryMovie),
    url(r'^queryActorByNation-(?P<nation>\d+)-(?P<pageid>\d+)',actor_view.queryActorByNation),
    url(r'^queryActor-(?P<id>\d+)',actor_view.queryActor)
]
