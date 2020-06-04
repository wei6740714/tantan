from pprint import pprint
from time import sleep

from django.core.cache import cache
from django.db import models
from django.http import HttpResponse, HttpRequest

# Create your views here.
from common import status_code
from lib.http import render_json
from lib.sms import send_verify_code, check_verify_code
from user.models import User
from user.models.user_model import UserForm


def get_verify_code(request:HttpRequest):

    '''验证码'''
    phonenum=request.GET.get('phonenum')
    return render_json(None) if send_verify_code(phonenum) else render_json(None,status_code.USER_SMS_SEND_FAIL)

    return render_json(None,status_code.USER_SMS_SEND_FAIL)


def login(request:HttpRequest):
    phonenum=request.POST.get('phonenum')
    verify_code=request.POST.get('verify_code')
    print(phonenum,verify_code,'******************')
    # 短信服务成功了,这里先忽略,判断
    # if not check_verify_code(phonenum,verify_code):
    #     return render_json(None,status_code.USER_VERIFY_FAIL)

    default_data={
        'nickname':phonenum,
        'phonenum':phonenum,
    }
    user,created=User.objects.get_or_create(phonenum=phonenum,defaults=default_data)

    request.session['uid'] = user.pk


    attr_dict=user.to_dict(('birth_year','birth_month','birth_day'))
    attr_dict['age']=user.age
    return render_json(attr_dict)




def show_profile(request):
    user=request.user
    profile=user.profile
    profile.save()
    print(profile.user)

    return render_json(profile.to_dict())


def modify_profile(request):
    '''Modify profile of user'''
    
    return render_json(None)


def upload_avatar(request):
    return render_json(None)


def modify_user(request:HttpRequest):

    user_form=UserForm(request.POST)

    if not user_form.is_valid():

        # pprint(user_form.errors)
        return render_json(None,status_code.HTTP_BAD)

    user=request.user

    return render_json(user_form.cleaned_data)