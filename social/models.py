from datetime import datetime

from django.db import models


# Create your models here.

class Swiper(models.Model):
    FLAG = (
        ('like', '喜欢'),
        ('superlike', '超级喜欢'),
        ('dislike', '不喜欢'),
    )
    # print(swiper.get_flag_display())

    user_id = models.IntegerField(verbose_name='用户')
    stranger_id = models.IntegerField(verbose_name='陌生人')
    create_datetime = models.DateTimeField(verbose_name='相识日期', auto_now=True)
    flag = models.CharField(max_length=32, choices=FLAG)

    @classmethod
    def like(cls, user_id, strange_id):
        user_id = user_id
        stranger_id = strange_id
        flag = 'like'

        obj=cls.objects.get_or_create(
            user_id=user_id,
            stranger_id=stranger_id,
            flag=flag,
        )

    @classmethod
    def superlike(cls, user_id, strange_id):
        user_id = user_id
        stranger_id = strange_id
        flag = 'superlike'
        cls.objects.get_or_create(
            user_id=user_id,
            stranger_id=stranger_id,
            flag=flag,
        )

    @classmethod
    def dislike(cls, user_id, strange_id):
        user_id = user_id
        stranger_id = strange_id
        flag = 'dislike'
        cls.objects.create(
            user_id=user_id,
            stranger_id=stranger_id,
            flag=flag,
        )


class Friends(models.Model):
    user1_id = models.IntegerField(verbose_name='用户1')
    user2_id = models.IntegerField(verbose_name='用户2')

    @classmethod
    def make_friend(cls,user1_id,user2_id):
        user1_id,user2_id=sorted((int(user1_id),int(user2_id)))

        cls.objects.get_or_create(
            user1_id=user1_id,
            user2_id=user2_id,
        )
