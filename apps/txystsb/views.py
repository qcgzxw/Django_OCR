import requests
import re
import base64
import json

from django.shortcuts import render
from django.http import HttpResponse
from main import Sign, Post, json2text

from txystsb.conf import app_id, secert_id, secert_key, bucket, urls, error_message


# Create your views here.
def index(request):
    '''
    首页
    '''
    return render(request, 'ocr.html')


def upload(request):
    '''
    图片上传
    '''
    s = Sign(app_id, bucket, secert_id, secert_key).__repr__()
    if request.method == 'GET':
        return HttpResponse('ERROR')
    elif request.method == 'POST':
        url_signal = int(request.POST['type'])
        obj = request.FILES.get('image')
        url = urls[url_signal % 8]
        headers = {'Host': 'recognition.image.myqcloud.com',
                   "Authorization": s
                   }

        files = {'appid': (None, app_id),
                 'bucket': (None, bucket),
                 'image': (obj.name, obj.read(), obj.content_type)
            }
        # 附加参数
        if url_signal % 8 == 0:
            files['card_type'] = (url_signal // 8 - 1)
        elif url_signal % 8 == 2:
            files['type'] = (url_signal // 8 - 1)

        # 备用参数
        payload = None 

        # 发送post请求
        post_image = Post(url=url, files=files, payload=payload,
                     headers=headers)
        r = post_image.send_image()
        responseinfo = r.content.decode('utf8')
        s = []
        d = {}
        res = json2text(url_signal % 8, json.loads(responseinfo))
        if type(res[0]) != type(d):
            s = res
        else:
            for k,v in res[0].items():
                s.append('<b>' + k + '</b>' + ' : ' + v + '<br>')
        return HttpResponse(s)# 返回识别信息