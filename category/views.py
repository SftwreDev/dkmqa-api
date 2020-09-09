from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Category1Serializer, Category2Serializer, Category3Serializer
from .models import Category1, Category2, Category3
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication\


############### Category 1 API List, Create , Update , Delete ###############


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category1API(request):
    if request.method == 'GET':
        cat1 = Category1.objects.all()
        serializer = Category1Serializer(cat1, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category1(request, pk):
    if request.method == 'PUT':
        cat1 = Category1.objects.get(id=pk)
        serializer = Category1Serializer(instance=cat1, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cat1 = Category1.objects.get(id=pk)
        cat1.delete()

        return Response("Item successfully deleted")




############### Category 2 API List, Create , Update , Delete ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category2API(request):
    if request.method == 'GET':
        cat2 = Category2.objects.all()
        serializer = Category2Serializer(cat2, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category2(request, pk):
    if request.method == 'PUT':
        cat2 = Category2.objects.get(id=pk)
        serializer = Category2Serializer(instance=cat2, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cat1 = Category2.objects.get(id=pk)
        cat1.delete()

        return Response("Item successfully deleted")


############### Category 3 API List, Create , Update , Delete ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category3API(request):
    if request.method == 'GET':
        cat3 = Category3.objects.all()
        serializer = Category3Serializer(cat3, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category3Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category3(request, pk):
    if request.method == 'PUT':
        cat3 = Category3.objects.get(id=pk)
        serializer = Category3Serializer(instance=cat3, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cat3 = Category3.objects.get(id=pk)
        cat3.delete()

        return Response("Item successfully deleted")