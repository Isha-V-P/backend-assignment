from functools import partial
from http.client import SERVICE_UNAVAILABLE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse,Http404
from rest_framework import status
from rest_framework.views import APIView
from .paginations import MyLimitOffsetPagination
from rest_framework.generics import ListAPIView
from api import serializers
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import generics

from rest_framework.pagination import (PageNumberPagination,LimitOffsetPagination)
from rest_framework import filters

from api.models import User
from api.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserAPI(APIView):

    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=UserSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except:
            raise Http404

    def get(self,request,id):
        user=self.get_object(id)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        user=self.get_object(id)
        serializer=UserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user=self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    filter_backends=(DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields=('first_name','last_name','company_name', 'city', 'state', 'zip', 'email', 'age', 'id', 'web', )
    #ordering_fields=('age',)
    search_fields=('first_name','last_name')
    pagination_class=MyLimitOffsetPagination