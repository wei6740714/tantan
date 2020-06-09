import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")
import django
django.setup()
from vip.models import Vip, Permission, VipPermission



def init_vip():
    for i in range(4):
        name = f'vip_{i}'
        Vip.objects.create(name=name, level=i)


PERMISSION_NAMES = {
    'get_rec_list':'获得推荐表功能',
    'like':'喜欢功能',
    'super_like':'超级喜欢功能',
    'dislike':'不喜欢功能',
    'show_liked_people':'显示喜欢过我的人功能',
}


def init_permission():
    for name,desc in PERMISSION_NAMES.items():
        Permission.objects.create(name=name,description=desc)


VIP_PERMISSION_RELATION={
    'vip_0':('get_rec_list','like'),
    'vip_1':('get_rec_list','like','super_like'),
    'vip_2':('get_rec_list','like','super_like','dislike'),
    'vip_3':('get_rec_list','like','super_like','dislike','show_liked_people'),
}

def create_vip_permission():

    for i in range(len(VIP_PERMISSION_RELATION)):

        vip_names = list(VIP_PERMISSION_RELATION.keys())
        permission_names = list(VIP_PERMISSION_RELATION.values())[i]
        vip_obj=Vip.objects.get(name=vip_names[i])

        for permission_name in permission_names:
            per=Permission.objects.get(name=permission_name)
            VipPermission.objects.create(vip_id=vip_obj.id,permission_id=per.id)




if __name__ == '__main__':
    init_vip()
    init_permission()
    create_vip_permission()