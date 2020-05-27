from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from lib.http import render_json


def get_verify_code(request):

    data={'code':1234,'name':'地一'};
    return render_json(data)



def login(request):

    return HttpResponse('login')


def show_profile(request):
    return HttpResponse('show_profile')


def modify_profile(request):
    return HttpResponse('modify_profile')


def upload_avatar(request):
    return HttpResponse('upload_avatar')