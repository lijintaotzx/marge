from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from user.serializers.user_serializer import UserRegisterSerializer


# Create your views here.


class UserRegView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def set_session(self, request, user):
        request.session['username'] = user.username
        request.session['user_id'] = user.pk

    def create(self, request, *args, **kwargs):
        s = UserRegisterSerializer(data=request.data)
        if s.is_valid():
            user = s.save()
            self.set_session(request, user)
            return Response({'msg': '注册成功！'}, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
