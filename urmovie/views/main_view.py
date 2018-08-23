# Author:Sunny Liu
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from urmovie import models
from django.views.decorators.csrf import csrf_exempt
''' 
    @id : 1
    @name : index
    @author : 刘旭阳
    @date : 2018.3.12
    @describe : 进入主页
'''
def index(request):
    return render(request,'index.html')

def movie_class(request):
    result =  models.Movie.objects.all()[:20]
    cate_list = models.Category.objects.all()
    age_list=[2018,2017,2016,2015,2014,2013,2012,2011,2010,2009]
    return render(request,'movie_category.html',{"movie":result,"cate":cate_list,"age":age_list})

def actor_class(request):
    result =  models.Actor.objects.all()[:20]
    return render(request,'actor_category.html',{"actor":result})


def contact(request):
    return render(request,'contact.html')