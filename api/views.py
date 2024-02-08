from django.shortcuts import render
from rest_framework.views import APIView

from api.serializers import SignUpSerializer,ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from api.models import Profile
from rest_framework import serializers
from rest_framework import authentication
from rest_framework import permissions


# Create your views here.

class SignUpView(APIView):

    def post(self,request,*args,**kwargs):
        seralizer=SignUpSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(data=seralizer.data)
        else:
            return Response (data=seralizer.errors)
    

class ProfileViewset(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def update(self,request,*args,**kwargs):
        user_obj=request.user.profile
        serializer=ProfileSerializer(data=request.data,instance=user_obj)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            u_obj = request.user.profile
            serializer = ProfileSerializer(instance=u_obj)
            return Response(data=serializer.data)
        else:
            return Response({'detail': 'User is not authenticated'})