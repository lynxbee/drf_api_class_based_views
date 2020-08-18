from django.urls import include, path

from helloproject.helloapp import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.users),
    path('user/<int:pk>/', views.user),
]
