# Author:Sunny Liu
from django.shortcuts import render
from django.db import models
from urmovie import models
"""
    内容简介：
        1.查询演员信息
        2.爬虫情况下，对演员信息的添加

"""
def queryActorByNation(request,nation,pageid):
    pageid = int(pageid)
    result = models.Actor.objects.filter(actor_nationality=nation).all()[(pageid-1)*2:pageid*2]
    return render(request, 'actor_category.html', {"actor": result})

def queryActor(request,id):
    result =  models.Actor.objects.filter(actor_id=id).first()
    movie = result.movie_set.all()
    return render(request,'actor_detail.html',{"actor":result})