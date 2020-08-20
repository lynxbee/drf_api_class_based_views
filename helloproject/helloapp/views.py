from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from helloproject.helloapp.models import UserInfo
from helloproject.helloapp.serializers import UserInfoSerializer

from django.views.decorators.csrf import csrf_exempt

class UserInfoView(viewsets.ModelViewSet) :
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

@csrf_exempt
def users(request):
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_by_pk(request, pk):
    if request.method == 'GET':
        users = UserInfo.objects.filter(pk=pk)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        user = UserInfo.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_by_name(request, user_name):
    if request.method == 'GET':
        users = UserInfo.objects.filter(username=user_name)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        user = UserInfo.objects.get(username=user_name)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_by_uuid(request, user_id):
    if request.method == 'GET':
        users = UserInfo.objects.filter(userid=user_id)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        user = UserInfo.objects.get(userid=user_id)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def index(request):
    return HttpResponse("This is Index page of user")

@csrf_exempt
def index_slug(request, custom_slug):
    return HttpResponse("This page accessed using Slug : " + custom_slug)
