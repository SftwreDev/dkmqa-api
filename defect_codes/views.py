from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  Category3Serializer, Category3DefectCodesSerializer, DefectCodesTranslationSerializers, DefectCodesTranslationStringSerializers
from .models import Defectcodes, DefectcodesTranslation
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from knox.auth import TokenAuthentication


############### Category 3 API List, Create , Update , Delete ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Category3API(request):
    if request.method == 'GET':
        cat3 = Defectcodes.objects.all()
        serializer = Category3DefectCodesSerializer(cat3, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = Category3Serializer(data=request.data)
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
def category3(request, pk):
    if request.method == 'GET':
        defect_codes = Defectcodes.objects.get(id=pk)
        serializer = Category3DefectCodesSerializer(instance=defect_codes, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        cat3 = Defectcodes.objects.get(id=pk)
        serializer = Category3Serializer(instance=cat3, data=request.data)
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
        cat3 = Defectcodes.objects.get(id=pk)
        cat3.delete()

        return Response("Item successfully deleted")


############### Defect Codes Translations API List, Create , Update , Delete ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def defect_codes_translation(request):
    if request.method == 'GET':
        translation = DefectcodesTranslation.objects.all()
        serializer = DefectCodesTranslationStringSerializers(translation, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = DefectCodesTranslationSerializers(data=request.data)
        request.data._mutable = True
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
def defect_codes_translation_edit_and_delete(request, pk):
    if request.method == 'GET':
        translation = DefectcodesTranslation.objects.get(id=pk)
        serializer = DefectCodesTranslationStringSerializers(instance=translation, many=False)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        translation = DefectcodesTranslation.objects.get(id=pk)
        serializer = DefectCodesTranslationSerializers(instance=translation, data=request.data)
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
        translation = DefectcodesTranslation.objects.get(id=pk)
        translation.delete()

        return Response("Item successfully deleted")
