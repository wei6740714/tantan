
from django.http import HttpRequest

# Create your views here.
from common import status_code
from lib.http import render_json
from lib.sms import send_verify_code, check_verify_code
from user.logic import save_avatar_to_location, save_avatar_to_remote
from user.models import User
from user.models import UserForm



def get_verify_code(request:HttpRequest):

    '''验证码'''
    phonenum=request.GET.get('phonenum')
    return render_json(None) if send_verify_code(phonenum) else render_json(None,status_code.USER_SMS_SEND_FAIL)




def login(request:HttpRequest):
    '''login operate'''
    phonenum=request.POST.get('phonenum')
    verify_code=request.POST.get('verify_code')
    # 短信服务成功了,这里先忽略,判断
    if not check_verify_code(phonenum,verify_code):
        return render_json(None,status_code.USER_VERIFY_FAIL)

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
    '''show profile detail'''
    user=request.user
    profile=user.profile
    profile.save()

    return render_json(profile.to_dict())


def modify_profile(request):
    '''Modify profile of user'''

    return render_json(None)


def upload_avatar(request:HttpRequest):
    '''upload profile avatar'''
    #Save image to location store
    save_path,file_name=save_avatar_to_location(request)

    #Save image to remote store
    save_avatar_to_remote(request,save_path,file_name)

    return render_json(None)


def modify_user(request:HttpRequest):
    '''modify user info'''
    user_form=UserForm(request.POST)
    if not user_form.is_valid():
        return render_json(None,status_code.HTTP_BAD)

    return render_json(user_form.cleaned_data)