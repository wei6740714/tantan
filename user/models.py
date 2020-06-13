from datetime import date

from django.db import models
from django import forms

from lib.base_model import MixinModel


class Profile(models.Model, MixinModel):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=99, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=16, choices=SEX, verbose_name='交友性别')
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matched = models.BooleanField(default=True, verbose_name='是否为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')



class User(models.Model, MixinModel):
    '''用户信息'''
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )

    nickname = models.CharField(max_length=32, verbose_name='呢称')
    phonenum = models.CharField(max_length=16, verbose_name='电话', unique=True)
    sex = models.CharField(max_length=16, verbose_name='性别', choices=SEX)
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='形象')
    location = models.CharField(max_length=16, verbose_name='常居地')

    @property
    def age(self):
        delta = date.today() - date(year=self.birth_year, month=self.birth_month, day=self.birth_day)
        return delta.days // 365

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(pk=self.id)
        self._profile: Profile
        return self._profile




class UserForm(forms.Form):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    nickname = forms.CharField(max_length=32)
    phonenum = forms.CharField(max_length=16)
    sex = forms.ChoiceField(choices=SEX)
    birth_year = forms.IntegerField(min_value=1)
    birth_month = forms.IntegerField(min_value=1, max_value=12)
    birth_day = forms.IntegerField(min_value=1, max_value=31)
    avatar = forms.CharField(max_length=256)
    location = forms.CharField(max_length=32)

    # 局部钩子
    # def clean_birth_year(self):
    #     val = self.cleaned_data.get("birth_year")
    #     if val.isdigit() and val<=12:
    #         return val
    #     else:
    #         raise ValidationError("用户名不能是纯数字!")











