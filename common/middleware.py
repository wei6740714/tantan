from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from kombu.utils import json

from common import error
from common.error import UserExceptionBase
from lib.http import render_json
from user.models import User


class MiddlewareAuth(MiddlewareMixin):
    white_list=[
        'api/user/vcode'
        'api/user/login'
    ]
    def process_request(self,request):
        if request.path in self.white_list:
            return None
        uid=request.session.get('uid')
        if not uid:
            return render_json(None, error.USER_NOT_LOGIN)
        try:
            user=User.objects.get(pk=uid)
        except User.DoesNotExist as e:
            return render_json(None, error.USER_DOES_NOT_EXIST)
        request.user=user
        return None

class MiddlewareException(MiddlewareMixin):
    def process_exception(self, request, exception):
        print(type(exception))
        print('Exception:', exception)
        if isinstance(exception,UserExceptionBase):
            return render_json(None,code=exception.code)




