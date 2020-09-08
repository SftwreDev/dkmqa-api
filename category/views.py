from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Category1Serializer, Category2Serializer, Category3Serializer
from .models import Category1, Category2, Category3
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication
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


@api_view(['POST'])
def category1_create_api(request):
    serializer = Category1Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_category1_api(request, pk):
    category1 = Category1.objects.get(id=pk)
    serializer = Category1Serializer(instance=category1, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category1_api(request, pk):
    category1 = Category1.objects.get(id=pk)
    category1.delete()

    return Response("Category 1 succesfully deleted")


############### Category 2 API List, Create , Update , Delete ###############

class Category2API(ListAPIView):
    serializer_class = Category2Serializer
    queryset = Category2.objects.all()


@api_view(['POST'])
def category2_create_api(request):
    serializer = Category2Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category2_api(request, pk):
    category1 = Category2.objects.get(id=pk)
    category1.delete()

    return Response("Category 2 succesfully deleted")


############### Category 3 API List, Create , Update , Delete ###############

class Category3API(ListAPIView):
    serializer_class = Category3Serializer
    queryset = Category3.objects.all()


@api_view(['POST'])
def category3_create_api(request):
    serializer = Category3Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category3_api(request, pk):
    category1 = Category3.objects.get(id=pk)
    category1.delete()

    return Response("Category 3 succesfully deleted")
