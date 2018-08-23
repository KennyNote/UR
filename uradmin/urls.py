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
from uradmin.views import crawl_view,user_view

"""
    URAdmin应用下的路由系统
"""
urlpatterns = [
    path('', user_view.login),
    path('index', user_view.login),
    path('detail_refresh',crawl_view.detail_refresh),
    path('crawltest',crawl_view.crawlMovieTest),
# path('', views.Login.as_view()),
]
