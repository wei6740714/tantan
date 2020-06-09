from django.shortcuts import render


# Create your views here.
from lib.http import render_json


def show_vip_permissions(request):
    
    return render_json(None)