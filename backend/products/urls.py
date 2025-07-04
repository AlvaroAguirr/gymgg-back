from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.ProductoListApi.as_view()),
    path('create', views.ProductoCreateApi.as_view()),
    path('detail/<pk>', views.ProductoDetailApi.as_view()),
    path('delete/<pk>', views.ProductoDeleteApi.as_view()),
    path('update/<pk>', views.ProductoUpdateApi.as_view())
]
