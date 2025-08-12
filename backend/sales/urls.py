from django.urls import path, include
from rest_framework import routers
from .views import SaleListCreateView


from . import views

urlpatterns= [
    path('', SaleListCreateView.as_view(), name='sales-list-create'),
    path('create',views.SaleCreateApi.as_view()),
    path('detail/<pk>', views.SaleDetailApi.as_view()),
    path('delete/<pk>',views.SaleDeleteApi.as_view()),
    path('update/<pk>',views.SaleUpdateApi.as_view())
]