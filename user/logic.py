import os

from tantan.settings import BASE_DIR, MEDIA_URL


def save_avatar_to_location(request):
    avatar_image =request.FILES.get('avatar')

    file_name='avatar'+str(request.user.id)+'.'+avatar_image.name.split('.')[-1]
    save_path=os.path.join(BASE_DIR,MEDIA_URL,file_name)

    with open(save_path ,'wb+') as f:
        print(f)
        for chunk in avatar_image.chunks():
            f.write(chunk)
    dirname=os.path.dirname(save_path)
    return save_path,file_name

def save_avatar_to_remote(request,save_path,file_name):

    import oss2

    ALIYUN_BUCKET_NAME='load-bar'
    ALIYUN_ACCESSKEY_ID='LTAI4GGWpaRTihWGSDSSKvpe'
    ALIYUN_ACCESSKEY_SECRET='2CKBpc1Sm77Jec6IEnQObBpE2E2qQ6'
    ENDPOINT =  'oss-cn-beijing.aliyuncs.com'#在区域链接中中可以找到该节点


    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth(ALIYUN_ACCESSKEY_ID, ALIYUN_ACCESSKEY_SECRET)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, ENDPOINT, ALIYUN_BUCKET_NAME)

    # os.path.join('avatar',str(request.user.id)+file_name)
    key='avatar'+'/'+file_name


    result = bucket.put_object_from_file(key, save_path)

    avatar_url=f'http://{ALIYUN_BUCKET_NAME}.{ENDPOINT}/{key}'
    user=request.user
    user.avatar=avatar_url
    user.save()




