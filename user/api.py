from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_verify_code(request):
    return HttpResponse('get_verify_code')


def login(request):

    return HttpResponse('login')


def show_profile(request):
    return HttpResponse('show_profile')


def modify_profile(request):
    return HttpResponse('modify_profile')


def upload_avatar(request):
    return HttpResponse('upload_avatar')