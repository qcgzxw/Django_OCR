import hmac
from hashlib import sha1
from time import time
from random import randrange
from base64 import b64encode
import requests

class Sign:
    def __init__(self, a, b, s, k):
        self.str = 'a=' + a + '&b=' + b + '&k=' + s + '&e=' \
                 + str(time()+2592000) + '&t=' + str(time()) \
                 + '&r=' + str(randrange(10**9, 10**10)) \
                 + '&u=0' + '&f='
        self.key = k

    def __str__(self):
        return self.str

    def __repr__(self):
        return b64encode(
                hmac.new(
                        self.key.encode('utf-8'), 
                        self.str.encode('utf-8'), 
                        sha1).digest() 
                + self.str.encode('utf-8'))


class Post:
    def __init__(self, url, headers, files=None, payload=None,):
        self.url = url
        self.headers = headers
        self.files = files
        self.payload = payload

    def send_image(self):
        if not self.payload:
            r = requests.post(self.url, headers = self.headers,
                files = self.files, )
        elif not self.files:
            r = requests.post(self.url, headers = self.headers,
                json = self.payload, )
        else:
            r = None
        return r

def json2text(signal, input):
    '''
    返回值处理
    '''
    if 'result_list' in input.keys():# 所有返回值统一处理
        input = input['result_list'][0]
    if input['code'] != 0:# 处理失败直接返回错误信息
        return input['message']
    res = []# 用于存放结果
    dic = {}# 用于临时存放结果
    if signal == 0:# 身份证
        if 'authority' in input['data'].keys():# 身份证反面
            dic['发证机关'] = input['data']['authority']
            dic['证件有效期'] = input['data']['valid_date']
        else:# 身份证正面
            dic['姓名'] = input['data']['name']
            dic['性别'] = input['data']['sex']
            dic['名族'] = input['data']['nation']
            dic['生日'] = input['data']['birth']
            dic['地址'] = input['data']['address']
            dic['身份证号'] = input['data']['id']
        res.append(dic)

    elif signal == 1:# 名片
        for item in input['data']:
            dic[item['item']] = item['value']
        res.append(dic)

    elif signal >= 2 or signal < 8:
        for item in input['data']['items']:
            if signal < 6:# 行驶证/驾驶证 车票 银行卡 营业执照
                dic[item['item']] = item['itemstring']
            else: # 印刷体 手写体
                res.append(item['itemstring']+'<br>')
        res.append(dic)

    else:
        return '参数错误'

    if {} == res[-1]:# 删除列表末尾多余的
        res.pop()
    return res