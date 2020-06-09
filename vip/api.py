from django.shortcuts import render


# Create your views here.
from lib.http import render_json
from vip.models import Vip


def show_vip_permissions(request):
    data={}
    for vip in Vip.objects.all():
        per_list=[]
        for per in vip.permissions:
            per_list.append(per.description)
        data[vip.name]=per_list
    print(data)
    return render_json(data)