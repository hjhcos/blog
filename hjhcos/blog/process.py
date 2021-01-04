from django.utils import timezone
from blog import models


# 获取文章
class Blog:

    def __init__(self):
        self.root = None
        self.date = None
        self.title = None
        self.url = None
        self.tag = None

    @staticmethod
    def show_tags():
        """ 打印所有tag"""
        tags = list(models.Blog.objects.values('tag'))
        tags = set([list(tag.values())[0] for tag in tags])
        return tags

    @staticmethod
    def get_file(url):
        """ 获取文件地址"""
        return models.Blog.objects.filter(url=url).first().file

    @staticmethod
    def get_single_all(title):
        """ 获取单文件所有信息 Blog.object"""
        return models.Blog.objects.filter(title=title).first()

    @staticmethod
    def get_all():
        """ 获取表后三个信息 Blog.object"""
        return models.Blog.objects.all().order_by('-uid')[:6]

    @staticmethod
    def write_data(title, tag, file):
        """ 写入数据"""
        date = timezone.now().date().strftime('%Y/%m/%d')
        models.Blog(
            date=date,
            title=title,
            tag=tag,
            url='/'+date+'/'+title,
            file=file,
            read=0
        ).save()


blog = Blog()
