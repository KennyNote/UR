# Author:Sunny Liu
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from urmovie import models
from django.views.decorators.csrf import csrf_exempt
import hashlib,os

"""
    内容简介：
        1.查询电影的信息
        2.爬虫情况下，对电影信息的添加

"""
def queryMovieByAge(request,age,pageid):
    pageid = int(pageid)
    cate_list = models.Category.objects.all()
    age_list=[2018,2017,2016,2015,2014,2013,2012,2011,2010,2009]
    result = models.Movie.objects.filter(movie_age=age).all()[(pageid-1)*2:pageid*2]
    return render(request, 'movie_category.html', {"movie": result, "cate": cate_list, "age": age_list})

def queryMovieByCate(request,cate,pageid):
    pageid = int(pageid)
    cate_list = models.Category.objects.all()
    age_list=[2018,2017,2016,2015,2014,2013,2012,2011,2010,2009]
    result = models.Movie.objects.filter(to_category__category_id=cate).all()[(pageid-1)*2:pageid*2]
    return render(request, 'movie_category.html', {"movie": result, "cate": cate_list, "age": age_list})

def queryMovie(request,id):
    result =  models.Movie.objects.filter(movie_id=id).first()
    comment = models.Comment.objects.filter(comment_belong=result).all()
    return render(request,'movie_detail.html',{"movie":result,"comment":comment})


def recommend(request,name):
    result = models.Movie.objects.filter(movie_name_en=name).first()
    comment = models.Comment.objects.filter(comment_belong=result).all()
    return render(request, 'movie_detail.html', {"movie": result, "comment": comment})