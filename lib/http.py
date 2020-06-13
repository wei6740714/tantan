import json

from django.http import HttpResponse

from common.error import HTTP_OK
from tantan.settings import DEBUG


def render_json(data,code=HTTP_OK):
    result={
        'data':data,
        'code':code,
    }
    if DEBUG:
        json_str = json.dumps(result,indent=4,ensure_ascii=False)
    else:
        json_str=json.dumps(result,separators=(',',':',),ensure_ascii=False)
    return HttpResponse(json_str)

