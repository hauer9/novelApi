import json

import requests


class Sms(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        data = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【分享阅读网】您的验证码是%s。如非本人操作，请忽略本短信' % code,
        }

        res = requests.post(self.url, data=data)
        re_dict = json.loads(res.text)
        return re_dict
