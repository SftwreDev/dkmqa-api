from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer , CategoryStringSerializer, CategoryTranslationSerializers, CategoryTranslationStringSerializers
from .models import Category , CategoryTranslation
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication


############### Category 1 API List, Create , Update , Delete ###############


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category1API(request):
    if request.method == 'GET':
        cat1 = Category.objects.all()
        serializer = CategoryStringSerializer(cat1, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = CategorySerializer(data=request.data)
        # request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['update_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    
    


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category1(request, pk):
    if request.method == 'GET':
        cat1 = Category.objects.filter(id=pk)
        serializer = CategoryStringSerializer(instance=cat1, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        cat1 = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=cat1, data=request.data)
        # request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['update_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        cat1 = Category.objects.get(id=pk)
        cat1.delete()

        return Response("Item successfully deleted")


############### Category 1 Translation API ###############


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category_translation(request):
    if request.method == 'GET':
        translation = CategoryTranslation.objects.all()
        serializer = CategoryTranslationStringSerializers(translation, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = CategoryTranslationSerializers(data=request.data)
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
def category_translation_update_and_delete(request, pk):
    if request.method == 'PUT':
        translation = CategoryTranslation.objects.get(id=pk)
        serializer = CategoryTranslationSerializers(instance=translation, data=request.data)
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
        translation = CategoryTranslation.objects.get(id=pk)
        translation.delete()

        return Response("Item successfully deleted")



