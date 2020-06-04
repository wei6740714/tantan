import hashlib
import json
from random import randrange
from time import time, sleep

import requests
from django.core.cache import cache

from tantan.config import WY_SMS_APPSECRET, WY_SMS_APPKEY
from worker import call_by_worker


def gen_verify_code(length):
    '''生成验证码'''
    min_value=10**(length-1)
    max_value=10**length
    return randrange(min_value,max_value)


@call_by_worker
def send_verify_code(phonenum):
    '''发送验证码'''
    # 生成验证码
    gen_code = gen_verify_code(6)
    # 通过接口发送验证码
    url = 'https://api.netease.im/sms/sendcode.action'
    #json类型
    data = {
        'mobile':phonenum,  #你的手机号码
        'codeLen':6,    # 定义验证码长度
        'authCode':gen_code, #要发送的验证码
    }
    Nonce = 'qweqdqwd12e01029i0dw0qwasddd'  #这个字符串时随机的长度不大于128，随便设
    CurTime = str(int((time() * 1000)))  #采用时间戳
    content =WY_SMS_APPSECRET + Nonce + CurTime
    CheckSum = hashlib.sha1(content.encode()).hexdigest()  #对上述进行按要求哈希
    headers = {   #设置请求头
        'AppKey':WY_SMS_APPKEY,
        'Nonce':Nonce,
        'CurTime':CurTime,
        'CheckSum':CheckSum
    }

    response = requests.post(url, data=data, headers=headers)#发送post请求
    str_result = response.text
    json_result = json.loads(str_result)

    status, verify_code = json_result['code'],json_result['obj']
    # if not status == status_code.USER_SMS_SEND_SUCCESS:
    #     return False
    #
    cache.set('verify_code' + phonenum, verify_code, timeout=60*60 * 24*5)

    return True


def check_verify_code(phonenum,verify_code):
    cache_verify_code = cache.get('verify_code' + phonenum)

    return cache_verify_code == verify_code





