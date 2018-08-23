from django.test import TestCase
from django.shortcuts import HttpResponse
from urmovie import models
from django.views import View
from django.shortcuts import render
import json
# Create your tests here.
"""
未完事项：
    增删改查时 对 Actor 和 Category 的级联操作没有完成
"""

#add电影信息
class add_test():
    def get(self, request):
        pass

    def post(self, request):
        ret = {'status': True, 'error': None, 'data': None}
        movie_dict = {
                      "movie_name_en": request.POST.get('movie_name_en', None),
                      "movie_name_cn": request.POST.get('movie_name_cn', None),
                      "movie_age": request.POST.get('movie_age', None),
                      "movie_where": request.POST.get('movie_where', None),
                      "movie_language": request.POST.get('movie_language', None),
                      "movie_date": request.POST.get('movie_date', None),
                      "movie_length": request.POST.get('movie_length', None),
                      "movie_director": request.POST.get('movie_director', None),
                      "movie_describe": request.POST.get('movie_describe', None)}
        models.Movie.objects.create(movie_dict)
        return HttpResponse(json.dumps(ret))

# update电影信息
class update_test(View):

    def get(self, request):
        pass

    def post(self, request):
        ret = {'status': True, 'error': None, 'data': None}
        obj = models.Movie.objects.filter(movie_id=request.POST.get('movie_id', None)).first()
        try:
            if obj:
                obj.movie_name_en =  request.POST.get('movie_name_en', None)
                obj.movie_name_cn = request.POST.get('movie_name_cn', None)
                obj.movie_age = request.POST.get('movie_age', None)
                obj.movie_where = request.POST.get('movie_where', None)
                obj.movie_language = request.POST.get('movie_language', None)
                obj.movie_date = request.POST.get('movie_date', None)
                obj.movie_length = request.POST.get('movie_length', None)
                obj.movie_director = request.POST.get('movie_director', None)
                obj.movie_describe = request.POST.get('movie_describe', None)
                obj.save()
            else:
                ret['status'] = False
                ret['error'] = "电影不存在"
        except Exception as e:
            ret['status'] = False
            ret['error'] = '请求错误'
        return HttpResponse(json.dumps(ret))

# delete电影信息
class delete_test(View):

    def get(self, request):
        ret = {'status': True, 'error': None, 'data': None}
        obj = models.Movie.objects.filter(movie_id=request.POST.get('movie_id', None)).first()
        try:
            if obj:
                models.Movie.objects.filter(movie_id=request.POST.get('movie_id', None)).delete()
            else:
                ret['status'] = False
                ret['error'] = "电影不存在"
        except Exception as e:
            ret['status'] = False
            ret['error'] = '请求错误'
        return HttpResponse(json.dumps(ret))

    def post(self, request):
        pass


class query_test(View):
    def get(self, request):
        movie = models.Movie.objects.filter(request.GET.get('movie_id', None)).first()
        return render(request, 'ur_admin/index.html', {'movie': movie})

    def post(self, request):
        pass
