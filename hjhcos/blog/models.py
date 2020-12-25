from django.db import models

# Create your models here.


class Blog(models.Model):

    uid = models.AutoField(primary_key=True, verbose_name='接口id')
    root = models.CharField(max_length=5, default='blog')
    date = models.DateField(auto_now_add=True, verbose_name='日期')
    title = models.CharField(max_length=10, verbose_name='标题')
    tag = models.CharField(max_length=10, verbose_name='标签')
    url = models.URLField(verbose_name='blog_URL')


class File(models.Model):

    title = models.CharField(max_length=10, verbose_name='标题')
    read = models.BigIntegerField(verbose_name='阅读量')
    # file will be saved to MEDIA_ROOT/blog/2020/12/30
    file = models.FileField(upload_to='blog/%Y/%m/%d/')
    api = models.ForeignKey(Blog)