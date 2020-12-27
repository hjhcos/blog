from django.db import models

# Create your models here.


class Api(models.Model):

    uid = models.AutoField(primary_key=True, verbose_name='api_id')
    date = models.CharField(max_length=11, verbose_name='日期')
    title = models.CharField(max_length=25, verbose_name='标题')
    tag = models.CharField(max_length=10, verbose_name='标签')
    url = models.CharField(max_length=25, verbose_name='api_url')
    file = models.CharField(max_length=256, verbose_name='api_file')
    read = models.BigIntegerField(verbose_name='阅读量')
