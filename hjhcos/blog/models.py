from django.db import models

# Create your models here.


class Blog(models.Model):

    uid = models.AutoField(primary_key=True)

    date = models.CharField(max_length=11, verbose_name='日期')   # 2020-12-30
    title = models.CharField(max_length=50, verbose_name='博客标题', unique=True)
    tag = models.CharField(max_length=8, verbose_name='标签')


class File(models.Model):
    api = models.OneToOneField(to='Blog', to_field='title')
    # file = models.FileField(verbose_name='api')
