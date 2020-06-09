from django.shortcuts import render

# Create your views here.
from lib.http import render_json
from social.logic import get_age_rec_list
from social.models import Swiper, Friends
from user.models import User
from vip.logic import expected_permission

@expected_permission(name='get_rec_list')
def get_rec_list(request):
    '''获取推荐列表'''
    # 根据年龄五岁之内的异性
    users = get_age_rec_list(request.user, 5)

    data = [user.to_dict() for user in users]
    return render_json(data)

@expected_permission(name='like')
def like(request):
    '''喜欢'''
    strange_id = request.POST.get('strange_id')

    Swiper.like(request.user.id, strange_id)
    Friends.make_friend(request.user.id, strange_id)
    return render_json(None)

@expected_permission(name='super_like')
def super_like(request):
    '''超级喜欢'''
    strange_id = request.POST.get('strange_id')

    Swiper.superlike(request.user.id, strange_id)
    Friends.make_friend(request.user.id, strange_id)

    return render_json(None)

@expected_permission(name='dislike')
def dislike(request):
    '''不喜欢'''
    strange_id = request.POST.get('strange_id')
    Swiper.dislike(request.user.id, strange_id)
    return render_json(None)

@expected_permission(name='show_liked_people')
def show_liked_people(request):
    '''查看喜欢过的人'''
    user=request.user
    like_list=Swiper.objects.filter(flag='like').filter(user_id=user.id)
    like_ids=[swiper.stranger_id for swiper in like_list]
    users=User.objects.filter(pk__in=like_ids)
    data=[user.to_dict() for user in users]


    return render_json(data)
