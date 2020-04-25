# coding=utf-8
# coding=utf-8
import requests
import json

from custom_lib.exceptions import DatabaseNotExists
from service.models import YunpianService

api_key = 'e99d437b73301715afd71e80438fc4f5'


class YunPian:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.api_key = YunpianService.objects.first().api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, mobile, text):
        # params = {
        #     'apikey': self.api_key,
        #     'mobile': mobile,
        #     'text': text,
        # }
        #
        # response = requests.post(self.single_send_url, data=params)
        # re_dict = json.loads(response.text)
        # return re_dict
        print(222222222222222)
        print(mobile)
        return True, '发送成功'
