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
        json_str = json.dumps(result,indent=4,ensure_ascii=True)
    else:
        json_str=json.dumps(result,separators=(',',':',))
    return HttpResponse(json_str)

