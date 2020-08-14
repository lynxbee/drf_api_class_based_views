from django.shortcuts import render
from rest_framework import viewsets

from helloproject.helloapp.models import UserInfo
from helloproject.helloapp.serializers import UserInfoSerializer

class UserInfoView(viewsets.ModelViewSet) :
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
# Create your views here.
