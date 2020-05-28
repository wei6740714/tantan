from time import sleep

from django.core.cache import cache
from django.http import HttpResponse, HttpRequest

# Create your views here.
from common import status_code
from lib.http import render_json
from lib.sms import send_verify_code, check_verify_code
from user.models import User


def get_verify_code(request:HttpRequest):

    '''验证码'''
    phonenum=request.GET.get('phonenum')
    print('***********')
    return render_json(None) if send_verify_code(phonenum) else render_json(None,status_code.USER_SMS_SEND_FAIL)



def login(request):
    phonenum=request.POST.get('phonenum')
    verify_code=request.POST.get('verify_code')

    if not check_verify_code(phonenum,verify_code):
        return render_json(None,status_code.USER_VERIFY_FAIL)

    user,created=User.objects.get_or_create(phonenum=phonenum)
    return render_json(user.to_dict())




def show_profile(request):

    return HttpResponse('show_profile')


def modify_profile(request):
    return HttpResponse('modify_profile')


def upload_avatar(request):
    return HttpResponse('upload_avatar')