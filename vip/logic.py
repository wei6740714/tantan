from functools import partial

from common.error import VipExceptedError, UserHttpBad
from vip.models import Vip


def expected_permission(func=None,name=None):
    if func is None:
        return partial(expected_permission,name=name)
    def wrapper(request):
        user=request.user
        print(user)
        try:
            print(user.vip_id)
            vip=Vip.objects.get(id=user.vip_id)
            names=[permission.name for permission in vip.permissions ]
            if name not in names:
                raise VipExceptedError('Excepted more high vip')
        except Vip.DoesNotExist as e:
            raise UserHttpBad('User not exist')
        return func(request)
    return wrapper