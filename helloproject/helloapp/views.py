from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from django.http import Http404
from django.http import HttpResponse, JsonResponse

from helloproject.helloapp.models import UserInfo
from helloproject.helloapp.serializers import UserInfoSerializer

class UserInfoView(viewsets.ModelViewSet) :
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class usersClassView(APIView):
    def get(self, request, format=None):
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self, request, format=None):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #refer https://www.lynxbee.com/how-to-delete-single-and-multiple-objects-in-django-drf/
    def delete(self, request, format=None):
        users = UserInfo.objects.all()
        if users:
            users.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_by_pk(APIView):
    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        users = UserInfo.objects.filter(pk=pk)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        user = UserInfo.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #refer https://www.lynxbee.com/how-to-delete-single-and-multiple-objects-in-django-drf/
    def delete(self, request, user_name, format=None):
        user = UserInfo.objects.filter(username=user_name)
        if user:
            user.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_by_name(APIView):
    def get(self, request, user_name, format=None):
        users = UserInfo.objects.filter(username=user_name)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_name, format=None):
        user = UserInfo.objects.get(username=user_name)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #refer https://www.lynxbee.com/how-to-delete-single-and-multiple-objects-in-django-drf/
    def delete(self, request, user_name, format=None):
        user = UserInfo.objects.filter(username=user_name)
        if user:
            user.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_by_uuid(APIView):
    def get(self, request, user_id, format=None):
        users = UserInfo.objects.filter(userid=user_id)
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_id, format=None):
        user = UserInfo.objects.get(userid=user_id)
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #refer https://www.lynxbee.com/how-to-delete-single-and-multiple-objects-in-django-drf/
    def delete(self, request, user_name, format=None):
        user = UserInfo.objects.filter(username=user_name)
        if user:
            user.delete()
            return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("This is Index page of user")

def index_slug(request, custom_slug):
    return HttpResponse("This page accessed using Slug : " + custom_slug)
