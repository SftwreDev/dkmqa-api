from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Category2Serializer, Category2ChecklistSerializer
from .models import Checklist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category2API(request):
    if request.method == 'GET':
        cat2 = Checklist.objects.all()
        serializer = Category2ChecklistSerializer(cat2, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category2Serializer(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['update_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category2(request, pk):
    if request.method == 'PUT':
        cat2 = Checklist.objects.get(id=pk)
        serializer = Category2Serializer(instance=cat2, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['update_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cat1 = Checklist.objects.get(id=pk)
        cat1.delete()

        return Response("Item successfully deleted")
