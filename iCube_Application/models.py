from django.db import models

# Create your models here.
# 先后执行下边两条命令
# manage.py makemigrations
# manage.py migrate
# models增删改查：https://blog.csdn.net/ZCF1002797280/article/details/49559863


class Article(models.Model):
    """
    AI 领域相关文章
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    image = models.URLField()
    article_text = models.TextField()
    source = models.CharField(max_length=50)


class User(models.Model):
    """
    用户表
    """
    phone = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=20)
    verification_code = models.CharField(max_length=4)
    user_name = models.CharField(max_length=20)


class ImageStyleChange(models.Model):
    """
    图像风格转换的表，用于记录转换结果，图片命名格式为<MD5值>.jpg
    """
    content_image = models.CharField(max_length=50)
    style_image = models.CharField(max_length=50)
    amazing_image = models.CharField(max_length=50)
