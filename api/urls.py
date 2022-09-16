from django.urls import path
from django.contrib import admin
from api.views import UserAPI,UserDetailAPI,UserListView#,UserAPIView


urlpatterns=[
    path('users/',UserAPI.as_view()),
    path('users/<int:id>/',UserDetailAPI.as_view()),
    path('users/usersearch/', UserListView.as_view())
]

