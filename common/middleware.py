from django.utils.deprecation import MiddlewareMixin

from common import status_code
from lib.http import render_json
from user.models import User


class MiddlewareAuth(MiddlewareMixin):
    white_list=[
        'api/user/vcode'
        'api/user/login'
    ]
    def process_request(self,request):
        print(request.path)
        if request.path in self.white_list:
            return
        uid=request.session.get('uid')
        if not uid:
            return render_json(None,status_code.USER_NOT_LOGIN)
        try:
            user=User.objects.get(pk=uid)
        except User.DoesNotExist as e:
            return render_json(None,status_code.USER_DOES_NOT_EXIST)
        request.user=user
        return
