import requests
import re
import base64

from django.shortcuts import render
from django.http import HttpResponse
from main import Sign, Post

from txystsb.conf import app_id, secert_id, secert_key, bucket, urls


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
        url = urls[url_signal]
        headers = {'Host': 'recognition.image.myqcloud.com',
                   "Authorization": s
                   }

        files = {'appid': (None, app_id),
                 'bucket': (None, bucket),
                 'image': (None, obj.read())
            }
        payload = None # 备用参数

        post_image = Post(url=url, files = files, payload=payload,
                     headers=headers)
        r = post_image.send_image()
        responseinfo = r.content
        print(responseinfo)
        return HttpResponse(responseinfo)# 只实现功能，暂时不处理数据