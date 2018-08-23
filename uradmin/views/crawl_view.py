# Author:Sunny Liu
from django.shortcuts import HttpResponse, render,redirect
from django.views.decorators.csrf import csrf_exempt
from urmovie import models
import urllib.request
import time
import os
import re
import datetime
import json
from django.http import JsonResponse
from django.core import serializers
import string

# 电影URL集合

# 获取电影列表(无错误)
def queryMovieList(count,movieUrls):
    url = "http://www.dytt8.net/html/gndy/dyzz/list_23_"+count+".html"
    conent = urllib.request.urlopen(url)
    conent = conent.read()
    conent = conent.decode('gb2312', 'ignore')
    pattern = re.compile('<div class="title_all"><h1><font color=#008800>.*?</a>></font></h1></div>' +
                         '(.*?)<td height="25" align="center" bgcolor="#F4FAE2"> ', re.S)
    items = re.findall(pattern, conent)
    str = ''.join(items)
    pattern = re.compile('<a href="(.*?)" class="ulink">(.*?)</a>.*?<td colspan.*?>(.*?)</td>', re.S)
    news = re.findall(pattern, str)
    for j in news:
        movieUrls.append('http://www.dytt8.net' + j[0])


def queryMovieInfo(movieUrls, resultlist):
    for index, item in enumerate(movieUrls):
        #创造headers用于伪装浏览器
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        item = urllib.request.Request(item, headers=headers)
        conent = urllib.request.urlopen(item)
        conent = conent.read()
        conent = conent.decode('gb2312', 'ignore')


        #页面内容处理
        #截取整个页面中所需要爬取信息的元素范围
        movieContent = re.findall(r'<div id="Zoom">(.*?)</div>', conent, re.S)
        pattern = re.compile('<br /><br />(.*?)<br /><br /><img')
        movieInfo = re.findall(pattern, movieContent[0])
        if not movieInfo:
            pattern = re.compile('<br /><br />(.*?)\r\n')
            movieInfo = re.findall(pattern, movieContent[0])
        if (len(movieInfo) > 0):
            movieInfo = movieInfo[0] + ''
            # 删除<br />标签
            movieInfo = movieInfo.replace("<br />", "")
            # 根据 ◎ 符号拆分
            movieInfo = movieInfo.split('◎')
        else:
            movieInfo = ""
        movie={}
        movie_dic = {"译名":"movie_name_en", "片名":"movie_name_cn", "年代":"movie_age",
                      "产地":"movie_where", "语言":"movie_language", "导演":"movie_director",
                      "简介":"movie_describe", "上映日期":"movie_date", "片长":"movie_length",
                      "类别":"movie_cate","主演":"movie_actor"}

        title_list = ["译名", "片名", "年代", "类别", "产地", "语言", "导演", "主演", "简介", "上映日期", "片长"]
        for line in movieInfo:
            title = line[0:4].replace("　　", "")
            detail = line[5:].replace("&middot;", "·").replace("&ldquo;", "“").replace("&rdquo;", "”") \
                .replace("&hellip;", "...").replace(" 　　　　　　", "/").replace(" 　　", "/").replace("&mdash;","—")
            if title in title_list:
                if title == "类别":
                    detail = list(detail.strip().split("/"))
                    movie[movie_dic[title]] = detail
                    print("title:" + title + "______" + "detail:", detail)
                elif title == "译名" or title == "片名":
                    detail = detail[:detail.find("/")]
                    movie[movie_dic[title]] = detail
                    print("title:" + title + "______" + "detail:", detail)
                elif title in ("导演", "主演"):
                    detail = re.sub(
                        "[\[\-\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\<\>\/\?\~\！\@\#\\\&\*\%]", "",
                        detail)
                    detail = re.sub("[A-Za-z0-9]{2,}","",detail)
                    detail = re.sub("[A-Za-z]\.","",detail)
                    detail = list(detail.split())
                    movie[movie_dic[title]] = detail
                    print("title:" + title + "______" + "detail:", detail)
                else:
                    movie[movie_dic[title]] = detail.strip()
                    print("title:" + title + "______" + "detail:", detail)
            else:
                pass


        # 电影海报
        pattern = re.compile('<img.*? src="(.*?)".*? />', re.S)
        movieImg = re.findall(pattern, movieContent[0])
        if (len(movieImg) > 0):
            movieImg = movieImg[0]
        else:
            movieImg = ""
        binary_data = urllib.request.urlopen(movieImg).read()
        base =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        url = base+"/media/movie_img/"+movie["movie_name_cn"] + ".jpg"
        with open(url, 'wb') as temp_file:
            temp_file.write(binary_data)

        #尝试直接读取图片 然后通过调用上传的功能转储到服务器
        new_movie = models.Movie(movie_name_en=movie["movie_name_en"],
                                 movie_name_cn=movie["movie_name_cn"],
                                 movie_age=movie["movie_age"],
                                 movie_where=movie["movie_where"],
                                 movie_language=movie["movie_language"],
                                 movie_date=movie["movie_date"],
                                 movie_length=movie["movie_length"],
                                 movie_describe=movie["movie_describe"],
                                 movie_director=movie["movie_director"][0],
                                 movie_image=url)
        new_movie.save()

        for i in range(len(movie["movie_cate"])):
            temp_cate = models.Category.objects.filter(category_name=movie["movie_cate"][i])
            if not temp_cate:
                new_cate = models.Category(category_name=movie["movie_cate"][i])
                new_cate.save()
                new_movie.to_category.add(new_cate)
            else:
                new_movie.to_category.add(temp_cate[0])

        for i in range(len(movie["movie_actor"])):
            temp_actor = models.Actor.objects.filter(actor_name=movie["movie_actor"][i])
            if not temp_actor:
                new_actor = models.Actor(actor_name=movie["movie_actor"][i],
                                         actor_gender="unknown",
                                         actor_birth=datetime.datetime.now(),
                                         actor_nationality="unknown")
                new_actor.save()
                new_movie.to_actor.add(new_actor)
            else:
                new_movie.to_actor.add(temp_actor[0])

        #resultlist.append(new_movie)
        time.sleep(2)

def crawlMovieTest(request):
    if request.method == 'POST':
        time = request.POST['time']
        count = int(request.POST['count'])
        host = request.POST['host']
        movieUrls = []
        resultlist = []
        if count < 25:
            queryMovieList('1', movieUrls)
            movieUrls = movieUrls[:count]
            queryMovieInfo(movieUrls, resultlist)
        else:
            page = (count//25)+1
            for i in range(1, page+1):
                queryMovieList(str(i), movieUrls)
            queryMovieInfo(movieUrls, resultlist)
        return render(request, 'ur_admin/index.html')


@csrf_exempt
def detail_refresh(request):
    if request.is_ajax():
        movielist = serializers.serialize("json", models.Movie.objects.all())
        return HttpResponse(movielist,content_type="application/json")