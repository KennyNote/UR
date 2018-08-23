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
def uploadImg(request,Movie):
    if request.method == 'POST':
        new_img = models.Image(
            image_file=request.FILES.get('img'),
            image_name = request.FILES.get('img').name,
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
'''
    @id : 3
    @name : pic_upload
    @author : 刘旭阳
    @date : 2018.3.12
    @describe : 上传文件
'''
def upload(request):

    obj = request.FILES.get('picture_upload')
    file_path = os.path.join('upload',obj.name)
    f = open(file_path, mode='wb')
    for item in obj.chunks():
        f.write(item)
    f.close()