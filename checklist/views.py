from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Category2Serializer, Category2ChecklistSerializer , ChecklistTranslationPostSerializers, ChecklistTranslationStringSerializer
from .models import Checklist , ChecklistTranslation
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication


########### Checklist API #################

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category2API(request):
    if request.method == 'GET':
        cat2 = Checklist.objects.all()
        serializer = Category2ChecklistSerializer(cat2, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category2Serializer(data=request.data)
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
def category2(request, pk):
    if request.method == 'GET':
        cat2 = Checklist.objects.get(id=pk)
        serializer = Category2ChecklistSerializer(instance=cat2, many=False)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        cat2 = Checklist.objects.get(id=pk)
        serializer = Category2Serializer(instance=cat2, data=request.data)
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
        cat1 = Checklist.objects.get(id=pk)
        cat1.delete()

        return Response("Item successfully deleted")


############ Checklist Translation API #################


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def translation_list_and_create(request):
    if request.method == 'GET':
        translation = ChecklistTranslation.objects.all()
        serializer = ChecklistTranslationStringSerializer(translation, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = ChecklistTranslationPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def translation_update_and_delete(request, pk):
    if request.method == 'PUT':
        translation = ChecklistTranslation.objects.get(id=pk)
        serializer = ChecklistTranslationPostSerializers(instance=translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        transaltion = ChecklistTranslation.objects.get(id=pk)
        translation.delete()
        return Response("Item successfully deleted")