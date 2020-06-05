
HTTP_OK=0

class UserExceptionBase(Exception):
    code=0

def generate_user_exception(cls_name,code):
    return type(cls_name, (UserExceptionBase,), {'code':code})

UserHttpOk=generate_user_exception('UserHttpOk',200)
UserHttpBad=generate_user_exception('UserHttpOk',201)
UserVerifyFail=generate_user_exception('UserVerifyFail',1001)
UserDoesNotExist=generate_user_exception('UserDoesNotExist',1002)
UserSmsSendFail=generate_user_exception('UserSmsSendFail',1003)
UserNotLogin=generate_user_exception('UserNotLogin',1004)