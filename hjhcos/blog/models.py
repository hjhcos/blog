from django.db import models

# Create your models here.


class Blog(models.Model):

    uid = models.AutoField(primary_key=True, verbose_name='blog_id')
    date = models.CharField(max_length=11, verbose_name='日期')
    title = models.CharField(max_length=25, verbose_name='标题')
    tag = models.CharField(max_length=10, verbose_name='标签')
    url = models.CharField(max_length=25, verbose_name='blog_url')
    file = models.CharField(max_length=256, verbose_name='blog_file')
    read = models.BigIntegerField(verbose_name='阅读量')
    text = models.CharField(max_length=256, verbose_name='截取内容')

