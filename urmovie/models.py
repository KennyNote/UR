from django.db import models


"""
    @id : 1
    @name : Movie
    @author : 刘旭阳
    @date : 2018.3.14
    @attribute : id(电影id),name_en(电影英文名),name_cn(电影中文名),age(电影年代),
                 where(电影产地),language(电影语言),date(电影上映日期),length(电影片长),
                 director(电影导演),actor(电影演员),describe(电影简介)
"""
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True,verbose_name="ID")
    movie_name_en = models.CharField(max_length=64,verbose_name="英文名")
    movie_name_cn = models.CharField(max_length=64,verbose_name="中文名")
    movie_age = models.IntegerField(verbose_name="年代")
    movie_where = models.CharField(max_length=32,verbose_name="产地")
    movie_language = models.CharField(max_length=32,verbose_name="语言")
    movie_date = models.CharField(max_length=255,verbose_name="上映日期")
    movie_length = models.CharField(max_length=255,verbose_name="片长")
    movie_director = models.CharField(max_length=128,verbose_name="导演")
    movie_describe = models.CharField(max_length=2000,verbose_name="简介")
    movie_image = models.CharField(max_length=255, verbose_name="封面")
    to_actor = models.ManyToManyField("Actor",verbose_name="演员")
    to_category = models.ManyToManyField("Category",verbose_name="类别")
    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

    def __str__(self):
        return self.movie_name_en +" "+ self.movie_name_cn

"""
    @id : 2
    @name : Category
    @author : 刘旭阳
    @date : 2018.3.14
    @attribute : id(电影类别id),name(电影类别)
"""
class Category(models.Model):
    category_id = models.AutoField(primary_key=True,verbose_name="ID")
    category_name = models.CharField(max_length=32,verbose_name="电影类别")

    class Meta:
        verbose_name = '电影类别'
        verbose_name_plural = '电影类别'

    def __str__(self):
        return self.category_name

"""
    @id : 3
    @name : Actor
    @author : 刘旭阳
    @date : 2018.3.14
    @attribute : id(演员id),name(演员姓名),gender(演员性别),birth(演员生日),nationality(演员国籍),
"""
class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True,verbose_name="ID")
    actor_name = models.CharField(max_length=32,verbose_name="演员姓名")
    actor_gender = models.CharField(max_length=32,verbose_name="演员性别")
    actor_birth = models.DateTimeField(verbose_name="演员生日")
    actor_nationality = models.CharField(max_length=32,verbose_name="演员国籍")
    class Meta:
        verbose_name = '演员'
        verbose_name_plural = '演员'

    def __str__(self):
        return self.actor_name

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True,verbose_name="ID")
    comment_author = models.CharField(max_length=50, verbose_name="评论作者")
    comment_detail = models.CharField(max_length=2000,verbose_name="评论详情")
    comment_belong = models.ForeignKey(to="Movie",to_field="movie_id",on_delete=models.CASCADE,verbose_name="评论源")
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.comment_detail





# """
#     @id : 4
#     @name : Movie2Class
#     @author : 刘旭阳
#     @date : 2018.3.14
#     @describe : movie 和 category 多对多关系
# """
#
# class Movie2Category(models.Model):
#     m2c_id = models.AutoField(primary_key=True)
#     movie = models.ForeignKey(to="Movie",to_field="movie_id",on_delete=models.DO_NOTHING,verbose_name="电影名")
#     movie_category = models.ForeignKey(to="Category",to_field="category_id",on_delete=models.DO_NOTHING,verbose_name="电影类别")
#
# """
#     @id : 5
#     @name : Movie2Actor
#     @author : 刘旭阳
#     @date : 2018.3.14
#     @describe : movie 和 actor 多对多关系
# """
#
# class Movie2Actor(models.Model):
#     m2a_id = models.AutoField(primary_key=True)
#     movie = models.ForeignKey(to="Movie",to_field="movie_id",on_delete=models.DO_NOTHING,verbose_name="电影名")
#     movie_actor = models.ForeignKey(to="Actor",to_field="actor_id",on_delete=models.DO_NOTHING,verbose_name="电影演员")
"python3 manage.py migrate urmovie"

"python3 manage.py makemigrations urmovie"
"python3 manage.py createsuperuser"
