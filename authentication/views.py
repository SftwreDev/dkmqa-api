from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken
from .serializers import UserSerializer , RegisterSerializer
from knox.auth import TokenAuthentication


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return HttpResponse({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
        else:
            return HttpResponse("Invalid username and password")







        

