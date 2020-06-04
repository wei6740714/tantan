from django.db import models

from lib.base_model import MixinModel
#


class Profile(models.Model ,MixinModel):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    location =models.CharField(max_length=32 ,verbose_name='目标城市')
    min_distance =models.IntegerField(default=1 ,verbose_name='最小查找范围')
    max_distance =models.IntegerField(default=10 ,verbose_name='最大查找范围')
    min_dating_age =models.IntegerField(default=18 ,verbose_name='最小交友年龄')
    max_dating_age =models.IntegerField(default=99 ,verbose_name='最大交友年龄')
    dating_sex =models.CharField(max_length=16 ,choices=SEX ,verbose_name='交友性别')
    vibration =models.BooleanField(default=True ,verbose_name='是否开启震动')
    only_matched =models.BooleanField(default=True ,verbose_name='是否为匹配的人看我的相册')
    auto_play =models.BooleanField(default=True ,verbose_name='自动播放视频')


    @property
    def user(self):
        from user.models import User
        if not hasattr(self, '_user'):
            try:
                self._user = User.objects.get(pk=self.id)
            except User.DoesNotExist:
                return None
        return self._user


