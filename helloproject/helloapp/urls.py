from django.urls import include, path
from rest_framework import routers

from helloproject.helloapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserInfoView)

urlpatterns = [
    path('', include(router.urls)),
]
