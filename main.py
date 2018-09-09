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
        return b64encode(hmac.new(self.key.encode('utf-8'), \
                         self.str.encode('utf-8'), sha1).digest() \
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