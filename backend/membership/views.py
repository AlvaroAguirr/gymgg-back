from django.shortcuts import render
from .models import Membership
from .serializers import MembershipSerializer
from rest_framework.permissions import AllowAny


from rest_framework.generics import (

    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)

class MembershipListApi(ListAPIView):
    serializer_class=MembershipSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Membership.objects.all()
    

class MembershipCreateApi(CreateAPIView):
    serializer_class=MembershipSerializer


# ver objeto especifi    
class MembershipDetailApi(RetrieveAPIView):
    serializer_class=MembershipSerializer


# delete objeto espeifico
class MembershipDeleteApi(DestroyAPIView):
    serializer_class=MembershipSerializer
    queryset=Membership.objects.filter()

class MembershipUpdateApi(UpdateAPIView):
    queryset= Membership.objects.all()
    serializer_class=MembershipSerializer


# Create your views here.
