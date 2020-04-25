# coding=utf-8
from rest_framework import serializers
from custom_lib.custom_seralizer_field import PhoneNumberField


class SendSmsSerializer(serializers.Serializer):
    pn = PhoneNumberField()
