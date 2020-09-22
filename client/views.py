from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ClientFormSerializers, ClientStringSerializers
from .models import Client


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
def client_list_and_create(request):
    if request.method == 'GET':
        client_list = Client.objects.all()
        serializer = ClientStringSerializers(client_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientFormSerializers(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializer.is_valid():
            serializer.save()
        else:
            content = { 'Error' : 'Invalid data' }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def client_update_and_delete(request, pk):
    if request.method == 'PUT':
        client = Client.objects.get(id=pk)
        serializer = ClientFormSerializers(instance=client, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        client = Client.objects.get(id=pk)
        client.delete()

        return Response("Item successfully deleted")
        