from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.UserListApi.as_view()),
    path('create', views.UserCreateApi.as_view()),
    path('detail/<pk>', views.UserDetailApi.as_view()),
    path('delete/<pk>', views.UserDeleteApi.as_view()),
    path('update/<pk>', views.UserUpdateApi.as_view()),
    path('categories/', views.MembershipListApi.as_view()),
]
