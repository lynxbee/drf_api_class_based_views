from rest_framework import serializers
from helloproject.helloapp.models import UserInfo, UserAddress

from drf_writable_nested import WritableNestedModelSerializer

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'home_no', 'street', 'city', 'pincode']

class UserInfoSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    useraddress = UserAddressSerializer(many=True)

    class Meta:
        model = UserInfo
        fields = ['id', 'userid', 'username', 'email', 'age', 'useraddress']
