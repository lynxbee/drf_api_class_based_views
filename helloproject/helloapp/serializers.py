from rest_framework import serializers
from helloproject.helloapp.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'age')
