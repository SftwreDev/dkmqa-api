from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import LanguageFormSerializers , LanguageStringSerializers

from .models import Language


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def language_list_and_create(request):
    if request.method == 'GET':
        language = Language.objects.all()
        serializer = LanguageStringSerializers(language, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageFormSerializers(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializer.is_valid():
            serializer.save()
        else:
            pass
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) 
def language_update_and_delete(request, pk):
    if request.method == 'PUT':
        language = Language.objects.get(id=pk)
        serializer = LanguageFormSerializers(instance=language, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            pass
        return Response(serializer.data)

    elif request.method == 'DELETE' :
        language = Language.objects.get(id=pk)
        language.delete()
    return Response('Item Successfully deleted')
  
