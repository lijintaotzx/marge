# coding=utf-8
from rest_framework import serializers

from .currency import match_pn


class PhoneNumberField(serializers.Field):

    def to_internal_value(self, data):
        if not match_pn(data):
            self.fail('pn')

        return data

    def to_representation(self, value):
        return value
