from django.urls import path, include
from rest_framework import routers



from . import views

urlpatterns= [
    path('',views.MembershipListApi.as_view()),
    path('create',views.MembershipCreateApi.as_view()),
    path('detail/<pk>', views.MembershipDetailApi.as_view()),
    path('delete/<pk>',views.MembershipDeleteApi.as_view()),
    path('update/<pk>',views.MembershipUpdateApi.as_view())
]