# coding=utf-8
from django.conf import settings
from django.core.cache import caches
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from custom_lib.currency import generate_code
from .lib.yunpian import YunPian
from .serializers.sms_service_serializer import SendSmsSerializer

cache = caches['service']


class SmsService(APIView):
    def post(self, request):
        s = SendSmsSerializer(data=request.data)
        if s.is_valid():
            pn = s.data['pn']
            code = generate_code()
            yunpian = YunPian()
            send_status, msg = yunpian.send_sms(pn, code)
            if send_status:
                cache.set('{}_v_code'.format(pn), code, settings.VCODE_EXPIRATION_INTEVAL)
                return Response('发送成功！', status=status.HTTP_200_OK)
            else:
                return Response('发送失败！msg:{}'.format(msg), status=status.HTTP_400_BAD_REQUEST)

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
