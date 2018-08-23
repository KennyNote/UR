from django.contrib import admin
import xadmin
from xadmin import views


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'UR电影资源管理系统'
    # 设置base_site.html的Footer
    site_footer = '刘旭阳'
    menu_style = 'accordion'
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

xadmin.site.register(views.CommAdminView, GlobalSetting)
# Register your models here.
from urmovie import models


"""
    admin.py
    把要使用的实体类注册到Django的杀手admin工具中去，
        通过Django 1.7新增加的@装饰器的方式替换原有将管理器和注册语句分开的方式
            list_display 是在Django后台中对要操作的类，显示可编辑字段的列表
            list_per_page 级联编辑时，一页显示的数据量
            filter_horizontal 要级联编辑的字段
"""
@xadmin.sites.register(models.Movie)
class MovieAdmin(object):
    list_display=('movie_id', 'movie_name_en', 'movie_name_cn', 'movie_age',
                  'movie_where', 'movie_language', 'movie_date', 'movie_length',
                  'to_category','movie_director', 'to_actor','movie_describe')
    list_per_page = 50
    list_filter = ('movie_name_en','movie_name_cn','movie_age','movie_where',
                   'movie_language','to_category','movie_director','to_actor')
    list_display_links = ("movie_id",)
    filter_horizontal = ('to_actor','to_category',)

@xadmin.sites.register(models.Category)
class CategoryAdmin(object):
    list_display=('category_id', 'category_name')
    list_display_links = ("category_name",)
    list_per_page = 10

@xadmin.sites.register(models.Actor)
class ActorAdmin(object):
    list_display=('actor_id', 'actor_name', 'actor_gender', 'actor_birth','actor_nationality')
    list_display_links = ("actor_name",)
    list_per_page = 50

@xadmin.sites.register(models.Comment)
class CommentAdmin(object):
    list_display=('comment_id', 'comment_author', 'comment_detail', 'comment_belong')
    list_display_links = ("actor_deatil",)
    list_per_page = 50

# @admin.register(models.Image)
# class MovieAdmin(admin.ModelAdmin):
#     list_display=('image_id', 'image_name', 'image_file')
#     list_per_page = 50