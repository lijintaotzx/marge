# coding=utf-8
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password_1 = serializers.CharField()
    password_2 = serializers.CharField()

    def check_user_exists(self, username):
        return User.objects.filter(username=username).count() != 0

    def validate(self, attrs):
        if attrs.get('password_1') != attrs.get('password_2'):
            raise serializers.ValidationError('两次输入的密码不一致！')
        elif self.check_user_exists(attrs['username']):
            raise serializers.ValidationError('用户已存在！')
        else:
            return attrs

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password1')
        return User.objects.create_user(username=username, password=password)
