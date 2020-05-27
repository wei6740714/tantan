from django.db import models


# Create your models here.
class User(models.Model):
    '''用户信息'''
    SEX=(
        ('男性','男性'),
        ('女性','女性'),
    )

    nickname = models.CharField(max_length=32, verbose_name='呢称',unique=True)
    phonenum=models.CharField(max_length=16,verbose_name='电话',unique=True)
    sex = models.CharField(max_length=16, verbose_name='性别',choices=SEX)
    birth_year = models.IntegerField(verbose_name='出生年')
    birth_month = models.IntegerField(verbose_name='出生月')
    birth_day = models.IntegerField(verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='形象')
    location = models.CharField(max_length=16, verbose_name='常居地')

class Profile(models.Model):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    location=models.CharField(max_length=32,verbose_name='目标城市')
    min_distance=models.IntegerField(default=1,verbose_name='最小查找范围')
    max_distance=models.IntegerField(default=10,verbose_name='最大查找范围')
    min_dating_age=models.IntegerField(default=18,verbose_name='最小交友年龄')
    max_dating_age=models.IntegerField(default=99,verbose_name='最大交友年龄')
    dating_sex=models.CharField(max_length=16,choices=SEX,verbose_name='交友性别')
    vibration=models.BooleanField(default=True,verbose_name='是否开启震动')
    only_matched=models.BooleanField(default=True,verbose_name='是否为匹配的人看我的相册')
    auto_play=models.BooleanField(default=True,verbose_name='自动播放视频')