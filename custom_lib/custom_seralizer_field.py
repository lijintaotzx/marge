# coding=utf-8
from rest_framework import serializers

from .currency import match_pn


class PhoneNumberField(serializers.Field):

    def to_internal_value(self, data):
        self.error_messages = {
            'error_pn': '请输入正确的手机号码！'
        }

        if not match_pn(data):
            self.fail('error_pn')

        return data

    def to_representation(self, value):
        return value
