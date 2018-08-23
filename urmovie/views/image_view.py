# Author:Sunny Liu
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from urmovie import models
from django.views.decorators.csrf import csrf_exempt
import hashlib,os

"""
    内容简介：
        1.爬虫情况下，对电影封面的添加

"""
@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        print(type(request.FILES.get('img')))
        new_img = models.Image(
            image_file=request.FILES.get('img'),
            image_name = "hahaha.jpg",
        )
        new_img.save()
    return render(request, 'uploadimg.html')

@csrf_exempt
def showImg(request):
    imgs = models.Image.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'showimg.html', content)